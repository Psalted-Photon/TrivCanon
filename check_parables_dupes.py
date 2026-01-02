import json

# Load all three parables difficulty files
parables_easy = json.load(open('app/public/questions/parables-teachings/easy.json', 'r', encoding='utf-8'))
parables_medium = json.load(open('app/public/questions/parables-teachings/medium.json', 'r', encoding='utf-8'))
parables_hard = json.load(open('app/public/questions/parables-teachings/hard.json', 'r', encoding='utf-8'))

print(f"Parables & Teachings question counts:")
print(f"  Easy: {len(parables_easy)}")
print(f"  Medium: {len(parables_medium)}")
print(f"  Hard: {len(parables_hard)}")

# Collect all parables questions
all_parables = parables_easy + parables_medium + parables_hard
all_questions_text = {q['question'] for q in all_parables}

print(f"\n  Total parables questions: {len(all_parables)}")
print(f"  Unique questions: {len(all_questions_text)}")

# Check for duplicates within parables files
seen = {}
duplicates = []

for q in all_parables:
    text = q['question']
    if text in seen:
        duplicates.append({
            'question': text,
            'id1': seen[text],
            'id2': q.get('id', 'no-id')
        })
    else:
        seen[text] = q.get('id', 'no-id')

if duplicates:
    print(f"\n❌ Found {len(duplicates)} duplicate questions in Parables & Teachings:")
    for d in duplicates[:10]:
        print(f"\n  '{d['question'][:60]}...'")
        print(f"    IDs: {d['id1']} and {d['id2']}")
else:
    print(f"\n✅ No duplicates found in Parables & Teachings files")

# Sample some questions to verify they are parables
print(f"\nSample Parables & Teachings - Hard questions:")
for i, q in enumerate(parables_hard[:5], 1):
    print(f"{i}. {q['question'][:70]}...")
