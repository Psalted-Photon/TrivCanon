#!/usr/bin/env python3
"""
Simple question adder - just paste AI response and it handles everything
"""

import json
import os
import sys
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

def main():
    stats = show_status()
    target = find_target(stats)
    
    if not target:
        return
    
    print(f"\n📝 Next target: {target['theme_name']} - {target['difficulty']}")
    print(f"   Current: {target['count']}, Need: {target['needed']}, Generating: {target['generate_count']}")
    
    # Load existing questions to show as "avoid"
    filepath = Path(target['filepath'])
    if filepath.exists():
        with open(filepath, 'r', encoding='utf-8') as f:
            existing = json.load(f)
    else:
        existing = []
    
    # Generate prompt
    print("\n" + "=" * 80)
    print("COPY THIS PROMPT:")
    print("=" * 80)
    print(f"Generate {target['generate_count']} Bible trivia questions for the TrivCanon app.")
    print(f"\nTHEME: {target['theme_name']}")
    print(f"DIFFICULTY: {target['difficulty']}")
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
    print(f"\nRULES:")
    print(f"1. Exactly 4 choices per question, correctIndex is 0-3")
    print(f"2. Use KJV Bible references only")
    print(f"3. All questions must be factually accurate and biblically correct")
    print(f"4. Difficulty \"{target['difficulty']}\": {'Basic facts, well-known stories' if target['difficulty'] == 'easy' else 'Moderate details, deeper knowledge' if target['difficulty'] == 'medium' else 'Obscure details, requires deep study'}")
    
    if existing:
        print(f"5. DO NOT duplicate or rephrase these existing questions:")
        print()
        for q in existing:
            print(f"- {q['question']}")
    
    print("\nOutput ONLY the JSON array, no other text.")
    print("=" * 80)
    
    # Wait for paste
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
        except EOFError:
            break
    
    if not lines:
        print("\n❌ No input received")
        return
    
    # Parse JSON
    json_text = '\n'.join(lines)
    
    # Clean up markdown code blocks if present
    json_text = json_text.strip()
    if json_text.startswith('```'):
        json_text = '\n'.join(json_text.split('\n')[1:])
    if json_text.endswith('```'):
        json_text = '\n'.join(json_text.split('\n')[:-1])
    json_text = json_text.strip()
    
    try:
        new_questions = json.loads(json_text)
    except json.JSONDecodeError as e:
        print(f"\n❌ Invalid JSON: {e}")
        return
    
    if not isinstance(new_questions, list):
        print("\n❌ Expected a JSON array")
        return
    
    print(f"\n✅ Parsed {len(new_questions)} questions")
    
    # Assign IDs and add theme/difficulty
    theme_code = target['theme_code']
    diff_code = target['diff_code']
    theme_name = target['theme_name']
    difficulty = target['difficulty']
    
    for q in new_questions:
        q['id'] = get_next_id(existing, theme_code, diff_code)
        q['theme'] = theme_name
        q['difficulty'] = difficulty
        existing.append(q)
    
    # Save
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Saved {len(new_questions)} questions to {filepath.name}")
    print(f"   New total: {len(existing)} questions")
    
    # Update index
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        index = json.load(f)
    
    for entry in index:
        if entry.get('themePath') == target['theme_folder'] and entry.get('difficulty') == difficulty:
            entry['count'] = len(existing)
    
    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Updated index.json")
    print(f"\n🎉 Done! Run script again to continue with next batch.")

if __name__ == "__main__":
    main()
