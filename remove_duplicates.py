import json
import os
from pathlib import Path

def remove_duplicates_from_file(filepath):
    """Remove duplicate questions from a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        questions = json.load(f)
    
    seen = {}
    unique_questions = []
    duplicates_removed = 0
    
    for q in questions:
        # Create a key based on question text, theme, and difficulty (case-insensitive)
        key = f"{q['question'].lower()}|{q['theme']}|{q['difficulty']}"
        
        if key not in seen:
            seen[key] = True
            unique_questions.append(q)
        else:
            duplicates_removed += 1
            print(f"  Removing duplicate: {q['id']} - {q['question'][:60]}...")
    
    if duplicates_removed > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(unique_questions, f, indent=2, ensure_ascii=False)
        print(f"  ✓ Removed {duplicates_removed} duplicate(s) from {os.path.basename(filepath)}")
    
    return duplicates_removed

def main():
    questions_dir = Path(r"c:\Users\Marlowe\Bible Trivia\app\public\questions")
    total_removed = 0
    files_modified = 0
    
    print("Scanning for duplicates...\n")
    
    for json_file in questions_dir.rglob("*.json"):
        if json_file.name == "index.json":
            continue
        
        print(f"\nChecking {json_file.relative_to(questions_dir)}...")
        removed = remove_duplicates_from_file(json_file)
        
        if removed > 0:
            files_modified += 1
            total_removed += removed
    
    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Files modified: {files_modified}")
    print(f"  Total duplicates removed: {total_removed}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
