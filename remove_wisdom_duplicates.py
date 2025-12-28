import json

with open('app/public/questions/wisdom-psalms/hard.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

print(f"Before cleanup: {len(questions)} questions")

# Remove duplicates by keeping only unique IDs
seen = set()
unique_questions = []
for q in questions:
    if q['id'] not in seen:
        seen.add(q['id'])
        unique_questions.append(q)

print(f"After cleanup: {len(unique_questions)} unique questions")

# Sort by ID
unique_questions.sort(key=lambda q: q['id'])

# Write back
with open('app/public/questions/wisdom-psalms/hard.json', 'w', encoding='utf-8') as f:
    json.dump(unique_questions, f, indent=2, ensure_ascii=False)

print("✅ Duplicates removed")
print(f"IDs: {unique_questions[0]['id']} to {unique_questions[-1]['id']}")
