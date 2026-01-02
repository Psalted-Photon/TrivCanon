import json
import re
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent

REQUIRED_KEYS = {"id","theme","question","choices","correctIndex","difficulty","reference","explanation","verses"}

ID_RE = re.compile(r"^[A-Z]{3}-[EMH]-\d{4}$")


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def audit_file(path: Path):
    data = load_json(path)
    issues = []

    if not isinstance(data, list):
        return [f"File root is not a JSON array: {path}"]

    # Duplicates by question text (exact)
    questions = [q.get("question") for q in data if isinstance(q, dict)]
    dupe_q = [q for q, c in Counter(questions).items() if q and c > 1]
    if dupe_q:
        issues.append(f"Duplicate question strings: {len(dupe_q)}")

    # Duplicates by id
    ids = [q.get("id") for q in data if isinstance(q, dict)]
    dupe_ids = [i for i, c in Counter(ids).items() if i and c > 1]
    if dupe_ids:
        issues.append(f"Duplicate ids: {len(dupe_ids)}")

    for idx, q in enumerate(data):
        if not isinstance(q, dict):
            issues.append(f"[{idx}] Not an object")
            continue

        missing = REQUIRED_KEYS - set(q.keys())
        if missing:
            issues.append(f"[{idx}] Missing keys: {sorted(missing)}")

        qid = q.get("id")
        if not isinstance(qid, str) or not ID_RE.match(qid):
            issues.append(f"[{idx}] Bad id format: {qid!r}")

        choices = q.get("choices")
        if not isinstance(choices, list) or len(choices) != 4 or not all(isinstance(c, str) for c in choices):
            issues.append(f"[{idx}] choices must be 4 strings")

        ci = q.get("correctIndex")
        if not isinstance(ci, int) or not (0 <= ci <= 3):
            issues.append(f"[{idx}] correctIndex out of range: {ci!r}")

        ref = q.get("reference")
        if not isinstance(ref, dict) or not all(k in ref for k in ("book","chapter","verse")):
            issues.append(f"[{idx}] reference missing book/chapter/verse")
        else:
            if not isinstance(ref.get("book"), str):
                issues.append(f"[{idx}] reference.book not string")
            if not isinstance(ref.get("chapter"), int):
                issues.append(f"[{idx}] reference.chapter not int")

        verses = q.get("verses")
        if not isinstance(verses, dict) or "kjv" not in verses or not isinstance(verses.get("kjv"), str) or not verses.get("kjv").strip():
            issues.append(f"[{idx}] verses.kjv missing/empty")

        # Simple ambiguity/quality heuristics
        qt = q.get("question")
        if isinstance(qt, str):
            if "Bible doesn't" in qt or "doesn't mention" in qt:
                issues.append(f"[{idx}] Meta-question (" + qid + ")")
            if qt.strip().endswith("?") is False:
                issues.append(f"[{idx}] question missing '?' ({qid})")

    return issues


def main():
    import argparse

    p = argparse.ArgumentParser()
    p.add_argument("file", help="Path to a questions json file")
    args = p.parse_args()

    path = Path(args.file)
    issues = audit_file(path)

    print(path)
    if not issues:
        print("✅ No structural issues found")
        return

    print(f"❌ Issues: {len(issues)}")
    for it in issues:
        print("-", it)


if __name__ == "__main__":
    main()
