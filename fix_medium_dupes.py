import json
from collections import Counter

# Load medium questions
with open('app/public/questions/apostles/medium.json', 'r', encoding='utf-8') as f:
    medium = json.load(f)

# Check for duplicate IDs
id_counts = Counter([q['id'] for q in medium])
duplicate_ids = {id: count for id, count in id_counts.items() if count > 1}

print(f"Total medium questions: {len(medium)}")
print(f"Unique IDs: {len(id_counts)}")
print(f"\nDuplicate IDs:")
for id, count in sorted(duplicate_ids.items()):
    print(f"  {id}: appears {count} times")
    
# Remove duplicates, keeping first occurrence
if duplicate_ids:
    seen = set()
    unique_questions = []
    removed = []
    
    for q in medium:
        if q['id'] not in seen:
            unique_questions.append(q)
            seen.add(q['id'])
        else:
            removed.append(q['id'])
    
    print(f"\nRemoving {len(removed)} duplicate entries...")
    
    # Save cleaned file
    with open('app/public/questions/apostles/medium.json', 'w', encoding='utf-8') as f:
        json.dump(unique_questions, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Cleaned medium.json: {len(unique_questions)} unique questions remain")
