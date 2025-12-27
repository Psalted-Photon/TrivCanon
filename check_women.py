import json

# Load current file
with open(r'c:\Users\Marlowe\Bible Trivia\app\public\questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

women = [q for q in data if q.get('theme') == 'Women of Faith']
print(f'Women of Faith count: {len(women)}')
print('\nFirst 10 Women of Faith questions:')
for i, q in enumerate(women[:10], 1):
    print(f'{i}. ID {q["id"]}: {q["question"]}')
