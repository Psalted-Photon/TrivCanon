import json

# Load all apostles question files
with open('app/public/questions/apostles/easy.json', 'r', encoding='utf-8') as f:
    easy = json.load(f)

with open('app/public/questions/apostles/medium.json', 'r', encoding='utf-8') as f:
    medium = json.load(f)

with open('app/public/questions/apostles/hard.json', 'r', encoding='utf-8') as f:
    hard = json.load(f)

# Display results
print(f"Easy: {len(easy)} questions (IDs: {easy[0]['id']} to {easy[-1]['id']})")
print(f"Medium: {len(medium)} questions (IDs: {medium[0]['id']} to {medium[-1]['id']})")
print(f"Hard: {len(hard)} questions (IDs: {hard[0]['id']} to {hard[-1]['id']})")
print(f"\nTotal Apostles questions: {len(easy) + len(medium) + len(hard)}")

# Check for duplicates
all_questions = easy + medium + hard
questions_text = [q['question'].lower().strip() for q in all_questions]
question_ids = [q['id'] for q in all_questions]

duplicates = []
seen = set()
for i, q in enumerate(questions_text):
    if q in seen:
        duplicates.append(question_ids[i])
    seen.add(q)

if duplicates:
    print(f"\n⚠️ WARNING: {len(duplicates)} duplicate questions found!")
    for dup_id in duplicates:
        print(f"  - {dup_id}")
else:
    print("\n✅ No duplicate questions found!")
