import json

with open('app/public/questions/women-of-faith/hard.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

questions = [q['question'] for q in data]
print(f'Total questions: {len(questions)}')

# Find duplicates
seen = {}
dupes = []
for q in questions:
    if q in seen:
        dupes.append(q)
    else:
        seen[q] = 1

print(f'\nDuplicates found: {len(dupes)}')
if dupes:
    for d in dupes:
        print(f'  - {d}')
else:
    print('  ✅ No duplicates!')

# Also check for very similar questions
print('\n--- All 50 questions ---')
for i, q in enumerate(questions, 1):
    print(f'{i:2d}. {q[:80]}{"..." if len(q) > 80 else ""}')
