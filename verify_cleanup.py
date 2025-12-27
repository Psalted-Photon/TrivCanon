import json

# Load cleaned file
with open(r'c:\Users\Marlowe\Bible Trivia\app\public\questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f'Total questions: {len(data)}')
print(f'First question ID: {data[0]["id"]}')
print(f'Last question ID: {data[-1]["id"]}')

# Check if IDs are sequential
ids = [q['id'] for q in data]
is_sequential = ids == list(range(1, len(data)+1))
print(f'IDs are sequential (1-{len(data)}): {is_sequential}')

# Check for unique questions
questions = [q['question'] for q in data]
is_unique = len(questions) == len(set(questions))
print(f'All questions are unique: {is_unique}')

# Theme distribution
from collections import Counter
themes = Counter(q['theme'] for q in data)
print(f'\nTheme distribution:')
for theme, count in sorted(themes.items()):
    print(f'  {theme}: {count} questions')
