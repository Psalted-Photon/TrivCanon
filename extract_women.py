import json

# Load original file
with open(r'C:\Users\Marlowe\Bible Trivia\original_questions.json', 'r', encoding='utf-8-sig') as f:
    original = json.load(f)

# Load current file
with open(r'C:\Users\Marlowe\Bible Trivia\app\public\questions.json', 'r', encoding='utf-8') as f:
    current = json.load(f)

# Extract Women of Faith questions from original
women_of_faith = [q for q in original if q.get('theme') == 'Women of Faith']

print(f"Found {len(women_of_faith)} Women of Faith questions in original file")
print(f"Current file has {len(current)} questions")

# Save Women of Faith questions
with open(r'C:\Users\Marlowe\Bible Trivia\women_of_faith_questions.json', 'w', encoding='utf-8') as f:
    json.dump(women_of_faith, f, indent=2, ensure_ascii=False)

print(f"\nWomen of Faith questions saved to women_of_faith_questions.json")

# Show first few
print(f"\nFirst 5 Women of Faith questions:")
for i, q in enumerate(women_of_faith[:5], 1):
    print(f"{i}. ID {q['id']}: {q['question']}")
