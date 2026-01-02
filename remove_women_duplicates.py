import json
import os

# Process each difficulty level
difficulties = ['easy', 'medium', 'hard']
base_path = 'app/public/questions/women-of-faith'

total_removed = 0

for difficulty in difficulties:
    file_path = os.path.join(base_path, f'{difficulty}.json')
    
    if not os.path.exists(file_path):
        print(f"⚠️  {difficulty}.json not found")
        continue
    
    # Load questions
    with open(file_path, 'r', encoding='utf-8') as f:
        questions = json.load(f)
    
    print(f'\n{"="*80}')
    print(f'Women of Faith - {difficulty.upper()}')
    print(f'{"="*80}')
    print(f'Total questions: {len(questions)}')
    
    # Find duplicates by question text
    seen_questions = {}
    duplicates = []
    unique_questions = []
    
    for q in questions:
        question_text = q['question']
        if question_text in seen_questions:
            duplicates.append({
                'id': q['id'],
                'question': q['question'],
                'duplicate_of_id': seen_questions[question_text]['id']
            })
        else:
            seen_questions[question_text] = q
            unique_questions.append(q)
    
    if duplicates:
        print(f'\n❌ Found {len(duplicates)} duplicate(s):')
        for d in duplicates:
            print(f"  {d['id']}: '{d['question'][:60]}...'")
            print(f"    → Duplicate of {d['duplicate_of_id']}")
        
        # Save cleaned file
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(unique_questions, f, indent=2, ensure_ascii=False)
        
        print(f'\n✅ Removed {len(duplicates)} duplicate(s)')
        print(f'New total: {len(unique_questions)} questions')
        total_removed += len(duplicates)
    else:
        print('✅ No duplicates found')

print(f'\n{"="*80}')
print(f'SUMMARY')
print(f'{"="*80}')
print(f'Total duplicates removed across all difficulties: {total_removed}')
