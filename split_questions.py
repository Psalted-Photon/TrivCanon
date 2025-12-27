import json
from collections import defaultdict

# Theme mapping
THEME_MAP = {
    'Miracles': {'code': 'MIR', 'path': 'miracles'},
    'Prophets': {'code': 'PRO', 'path': 'prophets'},
    'Apostles': {'code': 'APO', 'path': 'apostles'},
    'Kings & Rulers': {'code': 'KNG', 'path': 'kings-rulers'},
    'Women of Faith': {'code': 'WOF', 'path': 'women-of-faith'},
    'Battles & Conquests': {'code': 'BAT', 'path': 'battles-conquests'},
    'Parables & Teachings': {'code': 'PAR', 'path': 'parables-teachings'},
    'Creation & Origins': {'code': 'CRE', 'path': 'creation-origins'},
    'Prophecy & End Times': {'code': 'END', 'path': 'prophecy-end-times'},
    'Journeys & Exile': {'code': 'JRN', 'path': 'journeys-exile'},
    'Festivals & Customs': {'code': 'FES', 'path': 'festivals-customs'},
    'Wisdom & Psalms': {'code': 'WIS', 'path': 'wisdom-psalms'}
}

DIFFICULTY_MAP = {
    'easy': 'E',
    'medium': 'M',
    'hard': 'H'
}

# Load questions
with open(r'app\public\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

print(f"Loaded {len(questions)} questions")

# Group by theme and difficulty
grouped = defaultdict(lambda: defaultdict(list))
for q in questions:
    theme = q['theme']
    difficulty = q['difficulty']
    grouped[theme][difficulty].append(q)

# Assign new IDs and write files
index_data = []
total_written = 0

for theme, difficulties in grouped.items():
    theme_info = THEME_MAP[theme]
    theme_code = theme_info['code']
    theme_path = theme_info['path']
    
    for difficulty, questions_list in difficulties.items():
        diff_code = DIFFICULTY_MAP[difficulty]
        
        # Sort by original ID to maintain some order
        questions_list.sort(key=lambda x: x['id'])
        
        # Assign new IDs
        for idx, q in enumerate(questions_list, 1):
            new_id = f"{theme_code}-{diff_code}-{idx:04d}"
            q['id'] = new_id
        
        # Write to file
        file_path = f"app/public/questions/{theme_path}/{difficulty}.json"
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(questions_list, f, indent=2, ensure_ascii=False)
        
        total_written += len(questions_list)
        
        # Add to index
        index_data.append({
            'theme': theme,
            'themeCode': theme_code,
            'themePath': theme_path,
            'difficulty': difficulty,
            'difficultyCode': diff_code,
            'count': len(questions_list),
            'filePath': f"questions/{theme_path}/{difficulty}.json"
        })
        
        print(f"✓ {theme} - {difficulty}: {len(questions_list)} questions → {file_path}")

# Write index
with open(r'app\public\questions\index.json', 'w', encoding='utf-8') as f:
    json.dump(index_data, f, indent=2, ensure_ascii=False)

print(f"\n✓ Index created with {len(index_data)} files")
print(f"\nTotal questions written: {total_written}")
print(f"Original questions: {len(questions)}")
print(f"Verification: {'✓ PASS' if total_written == len(questions) else '✗ FAIL - MISMATCH!'}")
