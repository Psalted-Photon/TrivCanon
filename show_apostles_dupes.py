import json

# Load all apostles question files
with open('app/public/questions/apostles/easy.json', 'r', encoding='utf-8') as f:
    easy = json.load(f)

with open('app/public/questions/apostles/medium.json', 'r', encoding='utf-8') as f:
    medium = json.load(f)

with open('app/public/questions/apostles/hard.json', 'r', encoding='utf-8') as f:
    hard = json.load(f)

# Find duplicates
def find_duplicates(questions):
    seen = {}
    duplicates = []
    for q in questions:
        text = q['question'].lower().strip()
        if text in seen:
            duplicates.append({
                'duplicate_id': q['id'],
                'duplicate_text': q['question'],
                'original_id': seen[text]['id'],
                'original_text': seen[text]['question']
            })
        else:
            seen[text] = q
    return duplicates

print("=== EASY DUPLICATES ===")
easy_dupes = find_duplicates(easy)
for d in easy_dupes:
    print(f"\n{d['duplicate_id']}: {d['duplicate_text']}")
    print(f"Original: {d['original_id']}: {d['original_text']}")

print("\n=== MEDIUM DUPLICATES ===")
medium_dupes = find_duplicates(medium)
for d in medium_dupes:
    print(f"\n{d['duplicate_id']}: {d['duplicate_text']}")
    print(f"Original: {d['original_id']}: {d['original_text']}")

print("\n=== HARD DUPLICATES ===")
hard_dupes = find_duplicates(hard)
for d in hard_dupes:
    print(f"\n{d['duplicate_id']}: {d['duplicate_text']}")
    print(f"Original: {d['original_id']}: {d['original_text']}")

print(f"\n\nTotal duplicates: {len(easy_dupes) + len(medium_dupes) + len(hard_dupes)}")
