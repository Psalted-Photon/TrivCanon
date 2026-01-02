#!/usr/bin/env python3
"""add_questions_simple.py

Interactive question ingester for TrivCanon.

- User chooses a theme (1-12).
- Script processes that theme's easy/medium/hard files in one run.
- Paste AI JSON arrays; script validates strictly before saving.
"""

import json
import re
from pathlib import Path

QUESTIONS_DIR = Path("app/public/questions")
INDEX_FILE = Path("app/public/questions/index.json")

THEME_MAP = {
    'apostles': {'code': 'APO', 'name': 'Apostles'},
    'battles-conquests': {'code': 'BAT', 'name': 'Battles & Conquests'},
    'creation-origins': {'code': 'CRE', 'name': 'Creation & Origins'},
    'festivals-customs': {'code': 'FES', 'name': 'Festivals & Customs'},
    'journeys-exile': {'code': 'JRN', 'name': 'Journeys & Exile'},
    'kings-rulers': {'code': 'KNG', 'name': 'Kings & Rulers'},
    'miracles': {'code': 'MIR', 'name': 'Miracles'},
    'parables-teachings': {'code': 'PAR', 'name': 'Parables & Teachings'},
    'prophecy-end-times': {'code': 'END', 'name': 'Prophecy & End Times'},
    'prophets': {'code': 'PRO', 'name': 'Prophets'},
    'wisdom-psalms': {'code': 'WIS', 'name': 'Wisdom & Psalms'},
    'women-of-faith': {'code': 'WOM', 'name': 'Women of Faith'}
}

DIFF_MAP = {'easy': 'E', 'medium': 'M', 'hard': 'H'}

REQUIRED_KEYS = {"question", "choices", "correctIndex", "reference", "explanation", "verses"}
REQUIRED_REFERENCE_KEYS = {"book", "chapter", "verse"}

AVOID_LIST_PREVIEW_LIMIT = 12

# When prompting the model, request a small buffer of extra questions to
# compensate for validation/duplicate rejections, reducing the chance that a
# single paste comes up short.
GENERATION_BUFFER = 3


def choose_theme() -> dict:
    themes = list(THEME_MAP.items())
    print("\n" + "=" * 80)
    print("Choose a theme to work on:")
    print("=" * 80)
    for i, (theme_folder, theme_info) in enumerate(themes, start=1):
        print(f"{i:2d}) {theme_info['name']}  ({theme_folder})")

    while True:
        try:
            choice = input("\nEnter theme number (1-12) or q to quit: ").strip().lower()
        except KeyboardInterrupt:
            raise SystemExit(0)
        if choice in {"q", "quit", "exit"}:
            raise SystemExit(0)

        try:
            idx = int(choice)
        except ValueError:
            print("❌ Please enter a number (1-12) or q.")
            continue

        if 1 <= idx <= len(themes):
            theme_folder, theme_info = themes[idx - 1]
            return {
                "theme_folder": theme_folder,
                "theme_code": theme_info["code"],
                "theme_name": theme_info["name"],
            }

        print(f"❌ Please enter a number between 1 and {len(themes)}.")

def get_all_file_stats():
    """Get counts for all 36 files"""
    stats = []
    for theme_folder, theme_info in THEME_MAP.items():
        for difficulty in ['easy', 'medium', 'hard']:
            filepath = QUESTIONS_DIR / theme_folder / f"{difficulty}.json"
            if filepath.exists():
                with open(filepath, 'r', encoding='utf-8') as f:
                    questions = json.load(f)
                    count = len(questions)
            else:
                count = 0
            
            needed = max(0, 50 - count)
            stats.append({
                'theme_name': theme_info['name'],
                'theme_folder': theme_folder,
                'theme_code': theme_info['code'],
                'difficulty': difficulty,
                'diff_code': DIFF_MAP[difficulty],
                'count': count,
                'needed': needed,
                'filepath': str(filepath)
            })
    
    return stats

def show_status():
    """Display current status"""
    stats = get_all_file_stats()
    
    # Group by theme
    by_theme = {}
    total = 0
    total_needed = 0
    
    for s in stats:
        theme = s['theme_name']
        if theme not in by_theme:
            by_theme[theme] = {}
        by_theme[theme][s['difficulty']] = s
        total += s['count']
        total_needed += s['needed']
    
    print("=" * 80)
    print("TrivCanon Question Status")
    print("=" * 80)
    
    for theme in sorted(by_theme.keys()):
        print(f"\n{theme}:")
        for diff in ['easy', 'medium', 'hard']:
            s = by_theme[theme][diff]
            status = "[✓]" if s['needed'] == 0 else f"[need {s['needed']}]"
            print(f"  {diff:8}  {s['count']}/50  {status}")
    
    print("\n" + "-" * 80)
    print(f"Total: {total}/1800 questions ({total_needed} needed)")
    print("=" * 80)
    
    return stats

def find_target(stats):
    """Find file that needs most questions (capped at 84)"""
    # Sort by needed descending
    stats.sort(key=lambda x: x['needed'], reverse=True)
    
    target = stats[0]
    if target['needed'] == 0:
        print("\n🎉 All files complete!")
        return None
    
    # Cap at 84
    generate_count = min(target['needed'], 84)
    
    return {
        **target,
        'generate_count': generate_count
    }


def get_file_stats(theme_folder: str, theme_info: dict, difficulty: str) -> dict:
    filepath = QUESTIONS_DIR / theme_folder / f"{difficulty}.json"
    if filepath.exists():
        with open(filepath, 'r', encoding='utf-8') as f:
            questions = json.load(f)
    else:
        questions = []

    # Count based on list length; we may prune invalid/dupes later.
    count = len(questions)
    needed = max(0, 50 - count)
    return {
        'theme_name': theme_info['name'],
        'theme_folder': theme_folder,
        'theme_code': theme_info['code'],
        'difficulty': difficulty,
        'diff_code': DIFF_MAP[difficulty],
        'count': count,
        'needed': needed,
        'generate_count': min(needed, 84),
        'filepath': str(filepath),
        'existing_questions': questions,
    }


def prune_existing_in_place(existing: list) -> tuple[list, list]:
    """Return (kept, removed_log). Removes invalid objects and exact normalized dupes.

    removed_log entries: (reason, id, question)
    """
    kept = []
    removed = []
    seen_norm = set()

    for q in existing:
        if not isinstance(q, dict):
            removed.append(("not_object", None, None))
            continue
        errs = validate_question_obj(q)
        qtext = q.get("question", "")
        qid = q.get("id")
        if errs:
            removed.append(("invalid_existing", qid, qtext))
            continue
        norm = _normalize_question_text(qtext)
        if norm in seen_norm:
            removed.append(("duplicate_existing", qid, qtext))
            continue
        seen_norm.add(norm)
        kept.append(q)

    return kept, removed

def get_next_id(questions, theme_code, diff_code):
    """Find next sequential ID"""
    if not questions:
        return f"{theme_code}-{diff_code}-0001"
    
    # Extract numbers from existing IDs
    numbers = []
    for q in questions:
        q_id = q.get('id', '')
        if q_id.startswith(f"{theme_code}-{diff_code}-"):
            try:
                num = int(q_id.split('-')[-1])
                numbers.append(num)
            except:
                pass
    
    next_num = max(numbers) + 1 if numbers else 1
    return f"{theme_code}-{diff_code}-{next_num:04d}"


def _normalize_question_text(text: str) -> str:
    text = text or ""
    text = text.strip().lower()
    text = re.sub(r"\s+", " ", text)
    return text


def validate_question_obj(q: dict) -> list:
    errors = []
    if not isinstance(q, dict):
        return ["Question is not an object"]

    missing = sorted(REQUIRED_KEYS - set(q.keys()))
    if missing:
        errors.append(f"Missing keys: {', '.join(missing)}")

    question = q.get("question")
    if not isinstance(question, str) or not question.strip():
        errors.append("'question' must be a non-empty string")

    choices = q.get("choices")
    if not isinstance(choices, list) or len(choices) != 4 or not all(isinstance(c, str) and c.strip() for c in choices):
        errors.append("'choices' must be an array of exactly 4 non-empty strings")
    elif len({_normalize_question_text(c) for c in choices}) != 4:
        errors.append("'choices' must contain 4 distinct answers")

    ci = q.get("correctIndex")
    if not isinstance(ci, int) or ci not in (0, 1, 2, 3):
        errors.append("'correctIndex' must be an integer 0-3")

    ref = q.get("reference")
    if not isinstance(ref, dict) or not REQUIRED_REFERENCE_KEYS.issubset(ref.keys()):
        errors.append("'reference' must be an object with book/chapter/verse")
    else:
        if not isinstance(ref.get("book"), str) or not ref.get("book").strip():
            errors.append("reference.book must be a non-empty string")
        if not isinstance(ref.get("chapter"), int) or ref.get("chapter") <= 0:
            errors.append("reference.chapter must be a positive integer")
        if not isinstance(ref.get("verse"), str) or not ref.get("verse").strip():
            errors.append("reference.verse must be a non-empty string")

    exp = q.get("explanation")
    if not isinstance(exp, str) or not exp.strip():
        errors.append("'explanation' must be a non-empty string")

    verses = q.get("verses")
    if not isinstance(verses, dict) or "kjv" not in verses:
        errors.append("'verses' must be an object containing 'kjv'")
    else:
        if not isinstance(verses.get("kjv"), str) or not verses.get("kjv").strip():
            errors.append("verses.kjv must be a non-empty string")

    return errors


def audit_questions(questions: list) -> dict:
    id_list = [q.get("id") for q in questions if isinstance(q, dict)]
    id_dupes = sorted({i for i in id_list if i and id_list.count(i) > 1})

    q_texts = [_normalize_question_text(q.get("question", "")) for q in questions if isinstance(q, dict)]
    q_dupes = sorted({t for t in q_texts if t and q_texts.count(t) > 1})

    missing_qmark = []
    for q in questions:
        if not isinstance(q, dict):
            continue
        qt = (q.get("question") or "").strip()
        if qt and not qt.endswith("?"):
            missing_qmark.append(q.get("id") or qt[:60])

    return {
        "count": len(questions),
        "id_dupes": id_dupes,
        "question_dupes": q_dupes,
        "missing_qmark": missing_qmark,
    }


def _parse_verse_token_to_int(token: str) -> int | None:
    token = (token or "").strip()
    if not token:
        return None
    digits = "".join(ch for ch in token if ch.isdigit())
    if not digits:
        return None
    try:
        value = int(digits)
    except ValueError:
        return None
    return value if value > 0 else None


def base_verses_from_reference(ref: dict) -> set[str]:
    """Return base verse keys for a reference, counting ranges as multiple verses.

    Example: John 3:"16" -> {"John 3:16"}
             John 3:"16-18" -> {"John 3:16","John 3:17","John 3:18"}
             John 3:"16,18-19" -> {"John 3:16","John 3:18","John 3:19"}

    Scope is per theme+difficulty file; cross-difficulty duplicates are allowed.
    """
    if not isinstance(ref, dict):
        return set()

    book = (ref.get("book") or "").strip()
    chapter = ref.get("chapter")
    verse_field = (ref.get("verse") or "").strip()
    if not book or not isinstance(chapter, int) or chapter <= 0 or not verse_field:
        return set()

    keys: set[str] = set()
    # Normalize separators. We support commas and semicolons as separators.
    parts = [p.strip() for p in verse_field.replace(";", ",").split(",") if p.strip()]
    for part in parts:
        if "-" in part:
            left, right = part.split("-", 1)
            start = _parse_verse_token_to_int(left)
            end = _parse_verse_token_to_int(right)
            if start is None or end is None:
                continue
            if end < start:
                start, end = end, start
            # Safety cap to avoid pathological ranges.
            if end - start > 199:
                end = start + 199
            for v in range(start, end + 1):
                keys.add(f"{book} {chapter}:{v}")
        else:
            v = _parse_verse_token_to_int(part)
            if v is None:
                continue
            keys.add(f"{book} {chapter}:{v}")

    return keys


def collect_existing_base_verses(existing: list) -> set[str]:
    used: set[str] = set()
    for q in existing:
        if not isinstance(q, dict):
            continue
        used |= base_verses_from_reference(q.get("reference") or {})
    return used


def chapter_key_from_reference(ref: dict) -> str | None:
    """Return a Book+Chapter key like 'John 3'. Used for prompt guidance only."""
    if not isinstance(ref, dict):
        return None
    book = (ref.get("book") or "").strip()
    chapter = ref.get("chapter")
    if not book or not isinstance(chapter, int) or chapter <= 0:
        return None
    return f"{book} {chapter}"


def print_avoid_chapters_guidance(existing: list) -> None:
    """Print a chapter-level list to suggest variety.

    This is NOT enforced. Chapter reuse is allowed; only duplicate question text is rejected.
    """
    used: set[str] = set()
    for q in existing:
        if not isinstance(q, dict):
            continue
        key = chapter_key_from_reference(q.get("reference") or {})
        if key:
            used.add(key)

    if not used:
        return

    chapters = sorted(used)
    print(f"Chapters already used in this file (guidance only; {len(chapters)} total):")
    print()
    for ch_key in chapters:
        print(f"- {ch_key}")


def print_avoid_list(existing: list) -> None:
    # Backward-compatible name.
    print_avoid_chapters_guidance(existing)


def parse_pasted_json_array() -> list:
    print("\n📋 Paste the AI response (JSON array) below, then press Enter twice:")
    print("=" * 80)

    lines = []
    empty_count = 0
    while True:
        try:
            line = input()
            if not line.strip():
                empty_count += 1
                if empty_count >= 2:
                    break
            else:
                empty_count = 0
                lines.append(line)
        except KeyboardInterrupt:
            raise KeyboardInterrupt("Paste cancelled")
        except EOFError:
            break

    if not lines:
        raise ValueError("No input received")

    json_text = '\n'.join(lines).strip()
    if json_text.startswith('```'):
        json_text = '\n'.join(json_text.split('\n')[1:])
    if json_text.endswith('```'):
        json_text = '\n'.join(json_text.split('\n')[:-1])
    json_text = json_text.strip()

    new_questions = json.loads(json_text)
    if not isinstance(new_questions, list):
        raise ValueError("Expected a JSON array")
    return new_questions


def update_index_count(theme_folder: str, difficulty: str, new_count: int) -> None:
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        index = json.load(f)

    updated = False
    for entry in index:
        if entry.get('themePath') == theme_folder and entry.get('difficulty') == difficulty:
            entry['count'] = new_count
            updated = True
            break

    if not updated:
        raise RuntimeError(f"index.json missing entry for {theme_folder} {difficulty}")

    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)

def main():
    show_status()
    selected = choose_theme()

    theme_folder = selected["theme_folder"]
    theme_info = THEME_MAP[theme_folder]

    print(f"\n🧭 Theme selected: {selected['theme_name']} ({theme_folder})")
    print("This run will handle easy, medium, and hard for this theme.")

    for difficulty in ["easy", "medium", "hard"]:
        target = get_file_stats(theme_folder, theme_info, difficulty)

        filepath = Path(target['filepath'])
        existing_raw = target["existing_questions"]

        # If file is messy, prune invalid/dupes first so we can truly hit 50.
        existing, removed = prune_existing_in_place(existing_raw)
        if removed:
            print(f"\n🧹 {difficulty}: removed {len(removed)} bad/duplicate existing entries before adding")

        if len(existing) >= 50:
            if len(existing) > 50:
                existing = existing[:50]
                filepath.parent.mkdir(parents=True, exist_ok=True)
                with open(filepath, 'w', encoding='utf-8') as f:
                    json.dump(existing, f, indent=2, ensure_ascii=False)
                update_index_count(theme_folder, difficulty, len(existing))
                print(f"\n✂️  {difficulty}: trimmed to 50 to enforce cap")
            else:
                print(f"\n[✓] {difficulty}: already 50/50, skipping")
            continue

        # Continue prompting until we reach 50, unless user skips.
        while len(existing) < 50:
            needed_now = 50 - len(existing)
            target['generate_count'] = min(needed_now + GENERATION_BUFFER, 84)

            print("\n" + "=" * 80)
            print(f"COPY THIS PROMPT ({difficulty.upper()}):")
            print("=" * 80)
            print(f"Generate {target['generate_count']} Bible trivia questions for the TrivCanon app.")
            print(f"\nTHEME: {target['theme_name']}")
            print(f"DIFFICULTY: {difficulty}")
            print(f"\nREQUIRED JSON FORMAT (array of objects):")
            print('```json')
            print('[')
            print('  {')
            print('    "question": "Your question text?",')
            print('    "choices": ["Correct Answer", "Wrong 1", "Wrong 2", "Wrong 3"],')
            print('    "correctIndex": 0,')
            print('    "reference": {')
            print('      "book": "Genesis",')
            print('      "chapter": 1,')
            print('      "verse": "1"')
            print('    },')
            print('    "explanation": "Brief explanation of why this answer is correct.",')
            print('    "verses": {')
            print('      "kjv": "The exact KJV verse text that supports this answer."')
            print('    }')
            print('  }')
            print(']')
            print('```')
            print(f"\nSTRICT RULES:")
            print("1. Only truth straight from the Bible (no tradition/speculation)")
            print("2. KJV reference + KJV verse text required for each question")
            print("3. Exactly 4 choices; correctIndex must match the correct choice")
            print("4. Avoid any question requiring arithmetic totals unless the verse states the number")
            print("5. Prefer chapters NOT listed below (guidance only; not enforced).")

            print_avoid_list(existing)

            print("\nOutput ONLY the JSON array, no other text.")
            print("=" * 80)

            try:
                new_questions = parse_pasted_json_array()
            except KeyboardInterrupt:
                print(f"\n⏭️  {difficulty}: cancelled. Moving to next difficulty.")
                break
            except Exception as e:
                print(f"\n❌ {difficulty}: {e}")
                continue

            print(f"\n✅ Parsed {len(new_questions)} questions")

            existing_norm = {_normalize_question_text(q.get('question', '')) for q in existing if isinstance(q, dict)}
            accepted = []
            rejected = []
            for i, q in enumerate(new_questions, start=1):
                errs = validate_question_obj(q)
                if not errs:
                    norm = _normalize_question_text(q.get('question', ''))
                    if norm in existing_norm:
                        errs.append("Duplicate/rephrase of existing question (normalized match)")
                    else:
                        existing_norm.add(norm)

                if errs:
                    rejected.append((i, q.get('question', ''), errs))
                else:
                    accepted.append(q)

            if rejected:
                print(f"\n⚠️  Rejected {len(rejected)} questions (will NOT be saved):")
                for i, qtext, errs in rejected[:10]:
                    preview = (qtext or "").strip()
                    if len(preview) > 120:
                        preview = preview[:117] + "..."
                    print(f"  - #{i}: {preview} :: {errs[0]}")
                if len(rejected) > 10:
                    print(f"  ... plus {len(rejected) - 10} more")

                cont = input("Proceed saving accepted questions only? (y/n): ").strip().lower()
                if cont not in {"y", "yes"}:
                    print(f"Skipping this paste for {difficulty}.")
                    continue

            if not accepted:
                print(f"\n❌ {difficulty}: 0 accepted questions; paste again")
                continue

            remaining_slots = max(0, 50 - len(existing))
            if len(accepted) > remaining_slots:
                print(f"\nℹ️  {difficulty}: {len(accepted)} accepted but only {remaining_slots} needed to reach 50.")
                accepted = accepted[:remaining_slots]

            theme_code = target['theme_code']
            diff_code = target['diff_code']
            theme_name = target['theme_name']

            for q in accepted:
                q['id'] = get_next_id(existing, theme_code, diff_code)
                q['theme'] = theme_name
                q['difficulty'] = difficulty
                existing.append(q)

            filepath.parent.mkdir(parents=True, exist_ok=True)
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(existing, f, indent=2, ensure_ascii=False)

            update_index_count(theme_folder, difficulty, len(existing))

            print(f"✅ Saved {len(accepted)} questions to {filepath.name}")
            print(f"   New total: {len(existing)} questions")

            audit = audit_questions(existing)
            if audit["count"] > 50:
                print(f"⚠️  Audit: file has {audit['count']} questions (expected max 50)")
            if audit["id_dupes"]:
                print(f"⚠️  Audit: duplicate IDs found: {', '.join(audit['id_dupes'][:5])}")
            if audit["question_dupes"]:
                print(f"⚠️  Audit: duplicate question texts found (normalized): {len(audit['question_dupes'])}")
            if audit["missing_qmark"]:
                print(f"⚠️  Audit: questions missing '?': {len(audit['missing_qmark'])}")

            if len(existing) >= 50:
                break

    print("\n🎉 Theme run complete. Re-run script for another theme.")

if __name__ == "__main__":
    main()
