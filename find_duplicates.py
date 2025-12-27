import json

# Load all questions
with open(r'c:\Users\Marlowe\Bible Trivia\app\public\questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f'Total questions loaded: {len(data)}')

# Find duplicates by question text
questions_text = {}
duplicates = []

for q in data:
    question_text = q['question']
    if question_text in questions_text:
        duplicates.append({
            'id': q['id'],
            'question': q['question'],
            'duplicate_of': questions_text[question_text]
        })
    else:
        questions_text[question_text] = q['id']

print(f'\nDuplicates found: {len(duplicates)}')
print('=' * 80)

for d in duplicates:
    print(f"Question {d['id']}: '{d['question']}' is duplicate of Question {d['duplicate_of']}")

# Create deduplicated list
seen_questions = set()
unique_questions = []

for q in data:
    if q['question'] not in seen_questions:
        seen_questions.add(q['question'])
        unique_questions.append(q)

# Renumber questions
for i, q in enumerate(unique_questions, 1):
    q['id'] = i

print(f'\n' + '=' * 80)
print(f'Original count: {len(data)}')
print(f'Duplicates removed: {len(duplicates)}')
print(f'Final unique questions: {len(unique_questions)}')

# Save cleaned file
with open(r'c:\Users\Marlowe\Bible Trivia\app\public\questions.json', 'w', encoding='utf-8') as f:
    json.dump(unique_questions, f, indent=2, ensure_ascii=False)

print(f'\nCleaned file saved successfully!')
