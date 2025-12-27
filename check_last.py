import json

# Load current file
with open(r'c:\Users\Marlowe\Bible Trivia\app\public\questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f'Total questions: {len(data)}')
print(f'Last question ID: {data[-1]["id"]}')
print(f'Last question: {data[-1]["question"][:60]}...')
print(f'Last question theme: {data[-1]["theme"]}')

# Count Women of Faith
women_count = len([q for q in data if q.get('theme') == 'Women of Faith'])
print(f'\nWomen of Faith: {women_count}')
print(f'Need to add: {80 - women_count} more questions')
