#!/usr/bin/env python
"""Verify + de-duplicate TrivCanon question bank.

Goals (per user request):
- Scan all 36 question files under app/public/questions/<theme>/<difficulty>.json
- Ensure IDs are unique and sequential per file: THEME-DIFF-0001..0050
- Ensure no duplicate questions across the entire bank (normalized question match)
- Remove duplicates ONLY (no rewrites besides deletions), then renumber IDs

This script defaults to DRY RUN.

Usage:
  python verify_and_dedupe_all.py --dry-run
  python verify_and_dedupe_all.py --apply

Optional safeguards:
  --require-same-correct-choice  (only treat two items as dup if normalized correct choice matches)

Outputs a report and, when --apply is passed, rewrites the affected JSON files and updates index counts.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple


ROOT = Path(__file__).resolve().parent
QUESTIONS_DIR = ROOT / "app" / "public" / "questions"
INDEX_PATH = QUESTIONS_DIR / "index.json"

ID_RE = re.compile(r"^[A-Z]{3}-[EMH]-\d{4}$")


def _normalize_question_text(text: str) -> str:
    return re.sub(r"\\s+", " ", (text or "").strip().lower())


def _normalize_choice_text(text: str) -> str:
    return re.sub(r"\\s+", " ", (text or "").strip().lower())


@dataclass
class QLoc:
    file_path: Path
    index: int
    qid: str
    question_norm: str
    correct_choice_norm: str


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, obj: Any) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write("\n")


def list_question_files_from_index() -> List[Dict[str, Any]]:
    entries = load_json(INDEX_PATH)
    if not isinstance(entries, list):
        raise SystemExit(f"index.json should be a list: {INDEX_PATH}")
    return entries


def resolve_file(entry: Dict[str, Any]) -> Path:
    fp = entry.get("filePath")
    if not isinstance(fp, str):
        raise SystemExit(f"Bad index entry (filePath missing): {entry}")
    # index paths are like "questions/apostles/easy.json" relative to app/public/
    return ROOT / "app" / "public" / fp


def expected_id_prefix(entry: Dict[str, Any]) -> str:
    theme_code = entry["themeCode"]
    diff_code = entry["difficultyCode"]
    return f"{theme_code}-{diff_code}-"


def verify_and_build_locations(
    entries: List[Dict[str, Any]],
    require_same_correct_choice: bool,
) -> Tuple[List[str], Dict[str, List[QLoc]]]:
    errors: List[str] = []
    dup_map: Dict[str, List[QLoc]] = {}

    for entry in entries:
        qfile = resolve_file(entry)
        prefix = expected_id_prefix(entry)

        if not qfile.exists():
            errors.append(f"Missing file: {qfile}")
            continue

        data = load_json(qfile)
        if not isinstance(data, list):
            errors.append(f"{qfile}: expected a list of questions")
            continue

        # Count mismatch info (we'll fix index later if apply)
        count_in_index = entry.get("count")
        if isinstance(count_in_index, int) and count_in_index != len(data):
            errors.append(f"COUNT MISMATCH {qfile}: file has {len(data)} but index says {count_in_index}")

        for i, obj in enumerate(data):
            if not isinstance(obj, dict):
                errors.append(f"{qfile}[{i}]: not an object")
                continue

            qid = obj.get("id", "")
            if not isinstance(qid, str) or not qid:
                errors.append(f"{qfile}[{i}]: missing id")
                continue

            if not ID_RE.match(qid):
                errors.append(f"{qfile}[{i}]: id not in format THEME-DIFF-0000: {qid}")

            if not qid.startswith(prefix):
                errors.append(f"{qfile}[{i}]: id prefix mismatch (expected {prefix}*): {qid}")

            qtext = obj.get("question", "")
            if not isinstance(qtext, str) or not qtext.strip():
                errors.append(f"{qfile}[{i}]: missing question text")
                continue

            choices = obj.get("choices")
            if not isinstance(choices, list) or len(choices) != 4 or not all(isinstance(c, str) for c in choices):
                errors.append(f"{qfile}[{i}]: invalid choices")
                continue

            correct_index = obj.get("correctIndex")
            if not isinstance(correct_index, int) or not (0 <= correct_index <= 3):
                errors.append(f"{qfile}[{i}]: invalid correctIndex")
                continue

            question_norm = _normalize_question_text(qtext)
            correct_choice_norm = _normalize_choice_text(choices[correct_index])

            key = question_norm
            if require_same_correct_choice:
                key = f"{question_norm}||{correct_choice_norm}"

            dup_map.setdefault(key, []).append(
                QLoc(
                    file_path=qfile,
                    index=i,
                    qid=qid,
                    question_norm=question_norm,
                    correct_choice_norm=correct_choice_norm,
                )
            )

    return errors, dup_map


def choose_keep(candidate_objs: List[Dict[str, Any]]) -> int:
    """Return index of best item to keep among duplicates.

    Heuristic: prefer items with verses.kjv non-empty, valid reference, distinct choices.
    Ties broken by lowest id lexicographically.
    """

    def score(obj: Dict[str, Any]) -> Tuple[int, int, int, str]:
        verses = obj.get("verses")
        kjv_ok = 1 if isinstance(verses, dict) and isinstance(verses.get("kjv"), str) and verses.get("kjv").strip() else 0

        ref = obj.get("reference")
        ref_ok = 1 if isinstance(ref, dict) and isinstance(ref.get("book"), str) and isinstance(ref.get("chapter"), int) and isinstance(ref.get("verse"), str) else 0

        choices = obj.get("choices")
        distinct_ok = 1
        if isinstance(choices, list) and all(isinstance(c, str) for c in choices):
            distinct_ok = 1 if len(set(_normalize_choice_text(c) for c in choices)) == len(choices) else 0
        else:
            distinct_ok = 0

        qid = obj.get("id")
        qid_s = qid if isinstance(qid, str) else "ZZZ"
        return (kjv_ok, ref_ok, distinct_ok, qid_s)

    scored = [(score(o), idx) for idx, o in enumerate(candidate_objs)]
    scored.sort(reverse=True)
    return scored[0][1]


def apply_dedup_and_renumber(
    entries: List[Dict[str, Any]],
    dup_map: Dict[str, List[QLoc]],
    require_same_correct_choice: bool,
    make_backup: bool,
) -> Tuple[int, int]:
    removed_questions = 0
    removed_id_dups = 0

    # Load all files once
    by_file: Dict[Path, List[Dict[str, Any]]] = {}
    entry_by_file: Dict[Path, Dict[str, Any]] = {}
    for entry in entries:
        fp = resolve_file(entry)
        entry_by_file[fp] = entry
        by_file[fp] = load_json(fp)

    # Remove duplicate questions across the entire bank
    for key, locs in dup_map.items():
        if len(locs) <= 1:
            continue

        objs = [by_file[loc.file_path][loc.index] for loc in locs]
        keep_rel = choose_keep(objs)

        # Remove all but keep_rel
        for rel_idx, loc in enumerate(locs):
            if rel_idx == keep_rel:
                continue
            # mark removal by setting to None; later compact per file
            by_file[loc.file_path][loc.index] = None  # type: ignore[assignment]
            removed_questions += 1

    # Compact and count ID duplicates after removals per file
    for fp, items in list(by_file.items()):
        compacted = [it for it in items if it is not None]
        # Track duplicate IDs within file
        seen: set[str] = set()
        for it in compacted:
            qid = it.get("id")
            if isinstance(qid, str):
                if qid in seen:
                    removed_id_dups += 1
                else:
                    seen.add(qid)
        by_file[fp] = compacted

    # After deletions, each file may be < 50. Renumber to 0001..N (expected 50, but user will refill later)
    for fp, questions in by_file.items():
        entry = entry_by_file[fp]
        prefix = expected_id_prefix(entry)
        for idx, q in enumerate(questions, start=1):
            q["id"] = f"{prefix}{idx:04d}"

    # Backup then write
    if make_backup:
        backup_root = ROOT / "_backup_questions_before_dedupe"
        backup_root.mkdir(exist_ok=True)
        for fp in by_file.keys():
            rel = fp.relative_to(ROOT)
            dest = backup_root / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(fp, dest)

    for fp, questions in by_file.items():
        save_json(fp, questions)

    return removed_questions, removed_id_dups


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="Apply removals + renumber IDs")
    ap.add_argument("--dry-run", action="store_true", help="Report only (default)")
    ap.add_argument("--require-same-correct-choice", action="store_true", help="Only treat as duplicate if normalized correct choice also matches")
    ap.add_argument("--no-backup", action="store_true", help="Skip writing backup copies before editing")
    args = ap.parse_args()

    dry_run = True
    if args.apply:
        dry_run = False
    if args.dry_run:
        dry_run = True

    entries = list_question_files_from_index()

    errors, dup_map = verify_and_build_locations(entries, args.require_same_correct_choice)

    dup_question_groups = {k: v for k, v in dup_map.items() if len(v) > 1}

    print("=" * 80)
    print("VERIFY + DEDUPE REPORT")
    print("=" * 80)
    print(f"Index entries: {len(entries)}")
    print(f"Duplicate question groups (global): {len(dup_question_groups)}")

    if errors:
        print("\n-- Issues --")
        for e in errors:
            print("-", e)

    if dup_question_groups:
        print("\n-- Duplicate question groups (showing up to 50) --")
        shown = 0
        for key, locs in sorted(dup_question_groups.items(), key=lambda kv: (-len(kv[1]), kv[0])):
            print(f"\nGroup size={len(locs)} key={key[:120]}")
            for loc in locs:
                print(f"  - {loc.file_path.relative_to(ROOT)}[{loc.index}] id={loc.qid}")
            shown += 1
            if shown >= 50:
                print("\n... (truncated) ...")
                break

    # Duplicate IDs report (global)
    id_locs: Dict[str, List[str]] = {}
    for entry in entries:
        fp = resolve_file(entry)
        data = load_json(fp)
        for i, q in enumerate(data):
            qid = q.get("id")
            if isinstance(qid, str):
                id_locs.setdefault(qid, []).append(f"{fp.relative_to(ROOT)}[{i}]")

    dup_ids = {qid: locs for qid, locs in id_locs.items() if len(locs) > 1}
    print(f"\nDuplicate IDs (global): {len(dup_ids)}")
    if dup_ids:
        for qid, locs in sorted(dup_ids.items(), key=lambda kv: (-len(kv[1]), kv[0]))[:50]:
            print(f"- {qid}: {', '.join(locs)}")
        if len(dup_ids) > 50:
            print("... (truncated) ...")

    if dry_run:
        print("\nDRY RUN: no changes applied.")
        return

    print("\nAPPLYING: removing duplicates and renumbering IDs...")
    removed_questions, removed_id_dups = apply_dedup_and_renumber(
        entries,
        dup_map,
        args.require_same_correct_choice,
        make_backup=not args.no_backup,
    )

    print(f"Removed duplicate questions: {removed_questions}")
    print(f"(Info) Duplicate IDs previously existing within files encountered: {removed_id_dups}")

    # Update index counts
    os.system(f"python {str(ROOT / 'update_index_counts.py')}")


if __name__ == "__main__":
    main()
