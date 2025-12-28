import json

with open('app/public/questions/wisdom-psalms/hard.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

print(f"Total Wisdom & Psalms Hard questions: {len(questions)}")
print(f"First ID: {questions[0]['id']}")
print(f"Last ID: {questions[-1]['id']}")
print("\nAll IDs:")
for q in questions:
    print(f"  {q['id']}")
