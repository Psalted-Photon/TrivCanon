#!/usr/bin/env python3
"""
TrivCanon Question Generator - Manual Batch Tool
Run: python add_questions.py         -> Show status & generate prompt
Run: python add_questions.py merge   -> Merge new questions from new_questions.json
"""

import json
import os
import re
import sys
import sys
from pathlib import Path

# Configuration
QUESTIONS_DIR = Path(__file__).parent / "app" / "public" / "questions"
NEW_QUESTIONS_FILE = Path(__file__).parent / "new_questions.json"
TARGET_PER_FILE = 50
MAX_BATCH = 84

# Theme mappings
THEMES = {
    "apostles": ("APO", "Apostles"),
    "battles-conquests": ("BAT", "Battles & Conquests"),
    "creation-origins": ("CRE", "Creation & Origins"),
    "festivals-customs": ("FES", "Festivals & Customs"),
    "journeys-exile": ("JRN", "Journeys & Exile"),
    "kings-rulers": ("KNG", "Kings & Rulers"),
    "miracles": ("MIR", "Miracles"),
    "parables-teachings": ("PAR", "Parables & Teachings"),
    "prophecy-end-times": ("END", "Prophecy & End Times"),
    "prophets": ("PRO", "Prophets"),
    "wisdom-psalms": ("WIS", "Wisdom & Psalms"),
    "women-of-faith": ("WOM", "Women of Faith"),
}

DIFFICULTIES = {
    "easy": "E",
    "medium": "M", 
    "hard": "H",
}


def load_questions(filepath):
    """Load questions from a JSON file."""
    if not filepath.exists():
        return []
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def save_questions(filepath, questions):
    """Save questions to a JSON file."""
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)


def get_all_file_stats():
    """Get current question counts for all 36 files."""
    stats = []
    for theme_folder, (code, theme_name) in THEMES.items():
        theme_path = QUESTIONS_DIR / theme_folder
        for difficulty, diff_code in DIFFICULTIES.items():
            filepath = theme_path / f"{difficulty}.json"
            questions = load_questions(filepath)
            count = len(questions)
            needed = max(0, TARGET_PER_FILE - count)
            stats.append({
                "theme_folder": theme_folder,
                "theme_code": code,
                "theme_name": theme_name,
                "difficulty": difficulty,
                "diff_code": diff_code,
                "filepath": filepath,
                "count": count,
                "needed": needed,
            })
    return stats


def extract_keywords(question_text):
    """Extract significant keywords from a question for duplicate detection."""
    # Remove common question words and punctuation
    stop_words = {
        "which", "what", "who", "whom", "whose", "where", "when", "why", "how",
        "did", "does", "do", "was", "were", "is", "are", "the", "a", "an", "of",
        "in", "on", "at", "to", "for", "and", "or", "but", "with", "by", "from",
        "that", "this", "these", "those", "his", "her", "its", "their", "be",
        "been", "being", "have", "has", "had", "having", "also", "called", "known",
        "according", "bible", "scripture", "testament", "new", "old",
    }
    
    # Normalize and split
    text = question_text.lower()
    text = re.sub(r"[^\w\s]", " ", text)
    words = text.split()
    
    # Keep significant words (names, nouns, verbs)
    keywords = [w for w in words if w not in stop_words and len(w) > 2]
    return set(keywords)


def find_similar_questions(new_question, existing_questions, threshold=3):
    """Check if a new question is too similar to existing ones."""
    new_keywords = extract_keywords(new_question)
    similar = []
    
    for q in existing_questions:
        existing_keywords = extract_keywords(q.get("question", ""))
        overlap = new_keywords & existing_keywords
        if len(overlap) >= threshold:
            similar.append((q["question"], overlap))
    
    return similar


def get_next_id(questions, theme_code, diff_code):
    """Get the next sequential ID for a theme/difficulty."""
    prefix = f"{theme_code}-{diff_code}-"
    max_num = 0
    
    for q in questions:
        qid = q.get("id", "")
        if qid.startswith(prefix):
            try:
                num = int(qid[len(prefix):])
                max_num = max(max_num, num)
            except ValueError:
                pass
    
    return f"{prefix}{max_num + 1:04d}"


def show_status():
    """Display current status of all question files."""
    stats = get_all_file_stats()
    
    print("\n" + "=" * 70)
    print("TrivCanon Question Status")
    print("=" * 70)
    
    total_current = 0
    total_needed = 0
    
    # Group by theme
    current_theme = None
    for s in stats:
        if s["theme_name"] != current_theme:
            current_theme = s["theme_name"]
            print(f"\n{current_theme}:")
        
        status = "✓" if s["needed"] == 0 else f"need {s['needed']}"
        print(f"  {s['difficulty']:8} {s['count']:3}/50  [{status}]")
        total_current += s["count"]
        total_needed += s["needed"]
    
    print("\n" + "-" * 70)
    print(f"Total: {total_current}/1800 questions ({total_needed} needed)")
    print("=" * 70)
    
    return stats


def generate_prompt(stats):
    """Generate a prompt for the AI to create questions."""
    # Find the file that needs the most questions
    needy = [s for s in stats if s["needed"] > 0]
    if not needy:
        print("\n🎉 All files have 50+ questions! Goal reached!")
        return None
    
    # Sort by most needed
    needy.sort(key=lambda x: -x["needed"])
    target = needy[0]
    
    # How many to generate (cap at MAX_BATCH and what's needed)
    to_generate = min(target["needed"], MAX_BATCH)
    
    # Load existing questions to include in prompt for duplicate avoidance
    existing = load_questions(target["filepath"])
    existing_questions = [q.get("question", "") for q in existing]
    
    print(f"\n📝 Generating prompt for: {target['theme_name']} - {target['difficulty']}")
    print(f"   Current: {target['count']}, Need: {target['needed']}, Generating: {to_generate}")
    
    # Build the prompt
    prompt = f"""Generate {to_generate} Bible trivia questions for the TrivCanon app.

THEME: {target['theme_name']}
DIFFICULTY: {target['difficulty']}

REQUIRED JSON FORMAT (array of objects):
```json
[
  {{
    "question": "Your question text?",
    "choices": ["Correct Answer", "Wrong 1", "Wrong 2", "Wrong 3"],
    "correctIndex": 0,
    "reference": {{
      "book": "Genesis",
      "chapter": 1,
      "verse": "1"
    }},
    "explanation": "Brief explanation of why this answer is correct.",
    "verses": {{
      "kjv": "The exact KJV verse text that supports this answer."
    }}
  }}
]
```

RULES:
1. Exactly 4 choices per question, correctIndex is 0-3
2. Use KJV Bible references only
3. All questions must be factually accurate and biblically correct
4. Difficulty "{target['difficulty']}": {"Basic facts most Christians know" if target['difficulty'] == 'easy' else "Requires good Bible knowledge" if target['difficulty'] == 'medium' else "Obscure details, requires deep study"}
5. DO NOT duplicate or rephrase these existing questions:

{chr(10).join(f'- {q}' for q in existing_questions[:30])}
{"... and " + str(len(existing_questions) - 30) + " more (avoid similar topics)" if len(existing_questions) > 30 else ""}

Output ONLY the JSON array, no other text."""

    print("\n" + "=" * 70)
    print("COPY THIS PROMPT:")
    print("=" * 70)
    print(prompt)
    print("=" * 70)
    
    # Save target info for merge
    target_info = {
        "theme_folder": target["theme_folder"],
        "theme_code": target["theme_code"],
        "theme_name": target["theme_name"],
        "difficulty": target["difficulty"],
        "diff_code": target["diff_code"],
        "filepath": str(target["filepath"]),
    }
    
    target_file = Path(__file__).parent / ".question_target.json"
    with open(target_file, "w") as f:
        json.dump(target_info, f)
    
    print(f"\n💾 Target saved. After getting the response:")
    print(f"   1. Save the JSON array to: {NEW_QUESTIONS_FILE}")
    print(f"   2. Run: python add_questions.py merge")
    
    return prompt


def merge_questions():
    """Merge new questions from new_questions.json into the target file."""
    # Load target info
    target_file = Path(__file__).parent / ".question_target.json"
    if not target_file.exists():
        print("❌ No target set. Run 'python add_questions.py' first to generate a prompt.")
        return False
    
    with open(target_file, "r") as f:
        target = json.load(f)
    
    # Load new questions
    if not NEW_QUESTIONS_FILE.exists():
        print(f"❌ File not found: {NEW_QUESTIONS_FILE}")
        print("   Save the AI's JSON response to this file first.")
        return False
    
    try:
        with open(NEW_QUESTIONS_FILE, "r", encoding="utf-8") as f:
            content = f.read().strip()
            # Handle markdown code blocks
            if content.startswith("```"):
                content = re.sub(r"^```\w*\n?", "", content)
                content = re.sub(r"\n?```$", "", content)
            new_questions = json.loads(content)
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON in {NEW_QUESTIONS_FILE}: {e}")
        return False
    
    if not isinstance(new_questions, list):
        print("❌ Expected a JSON array of questions.")
        return False
    
    print(f"\n📥 Loading {len(new_questions)} new questions...")
    print(f"   Target: {target['theme_name']} - {target['difficulty']}")
    
    # Load existing questions
    filepath = Path(target["filepath"])
    existing = load_questions(filepath)
    
    # Validate and process each new question
    added = []
    skipped = []
    duplicates = []
    
    for i, q in enumerate(new_questions):
        # Validate required fields
        required = ["question", "choices", "correctIndex", "reference", "explanation", "verses"]
        missing = [f for f in required if f not in q]
        if missing:
            skipped.append((i + 1, f"Missing fields: {missing}"))
            continue
        
        if not isinstance(q["choices"], list) or len(q["choices"]) != 4:
            skipped.append((i + 1, "Must have exactly 4 choices"))
            continue
        
        if q["correctIndex"] not in [0, 1, 2, 3]:
            skipped.append((i + 1, "correctIndex must be 0-3"))
            continue
        
        # Check for duplicates
        similar = find_similar_questions(q["question"], existing + added)
        if similar:
            duplicates.append((i + 1, q["question"], similar[0]))
            continue
        
        # Assign ID and metadata
        q["id"] = get_next_id(existing + added, target["theme_code"], target["diff_code"])
        q["theme"] = target["theme_name"]
        q["difficulty"] = target["difficulty"]
        
        added.append(q)
    
    # Report results
    print(f"\n📊 Results:")
    print(f"   ✓ Added: {len(added)}")
    
    if skipped:
        print(f"   ⚠ Skipped (invalid): {len(skipped)}")
        for num, reason in skipped[:5]:
            print(f"      Question {num}: {reason}")
    
    if duplicates:
        print(f"   ⚠ Skipped (similar to existing): {len(duplicates)}")
        for num, new_q, (existing_q, overlap) in duplicates[:5]:
            print(f"      Q{num}: \"{new_q[:50]}...\"")
            print(f"         Similar to: \"{existing_q[:50]}...\"")
            print(f"         Overlap: {overlap}")
    
    if not added:
        print("\n❌ No questions to add.")
        return False
    
    # Confirm before saving (skip if -y flag)
    print(f"\n📁 Will add {len(added)} questions to {filepath.name}")
    if "-y" not in sys.argv:
        response = input("   Proceed? (y/n): ").strip().lower()
        
        if response != "y":
            print("   Cancelled.")
            return False
    else:
        print("   Auto-confirming...")
    
    # Save
    all_questions = existing + added
    save_questions(filepath, all_questions)
    print(f"   ✓ Saved! New total: {len(all_questions)} questions")
    
    # Update index.json
    update_index()
    
    # Cleanup
    os.remove(NEW_QUESTIONS_FILE)
    os.remove(target_file)
    print(f"   ✓ Cleaned up temp files")
    
    return True


def update_index():
    """Update the index.json with current question counts."""
    index_path = QUESTIONS_DIR / "index.json"
    
    if not index_path.exists():
        print("   ⚠ index.json not found, skipping update")
        return
    
    with open(index_path, "r", encoding="utf-8") as f:
        index = json.load(f)
    
    # index.json is an array of entries, each with themePath and difficulty
    for entry in index:
        theme_path = entry.get("themePath", "")
        difficulty = entry.get("difficulty", "")
        if theme_path and difficulty:
            filepath = QUESTIONS_DIR / theme_path / f"{difficulty}.json"
            questions = load_questions(filepath)
            entry["count"] = len(questions)
    
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2)
    
    print("   ✓ Updated index.json")


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "merge":
        merge_questions()
    else:
        stats = show_status()
        generate_prompt(stats)


if __name__ == "__main__":
    main()
