import json

# Load all three parables difficulty files
parables_easy = json.load(open('app/public/questions/parables-teachings/easy.json', 'r', encoding='utf-8'))
parables_medium = json.load(open('app/public/questions/parables-teachings/medium.json', 'r', encoding='utf-8'))
parables_hard = json.load(open('app/public/questions/parables-teachings/hard.json', 'r', encoding='utf-8'))

print("Checking for duplicates across all Parables & Teachings files...")

# Find the duplicate
seen_questions = {}
duplicates_to_remove = []

for difficulty, questions, filename in [
    ('easy', parables_easy, 'easy.json'),
    ('medium', parables_medium, 'medium.json'),
    ('hard', parables_hard, 'hard.json')
]:
    for q in questions:
        text = q['question']
        q_id = q.get('id', 'no-id')
        
        if text in seen_questions:
            print(f"\n❌ Duplicate found:")
            print(f"   First: {seen_questions[text]['id']} in {seen_questions[text]['file']}")
            print(f"   Duplicate: {q_id} in {filename}")
            print(f"   Question: '{text[:80]}...'")
            duplicates_to_remove.append((filename, q_id))
        else:
            seen_questions[text] = {'id': q_id, 'file': filename}

# Remove duplicates
if duplicates_to_remove:
    for filename, q_id in duplicates_to_remove:
        if filename == 'easy.json':
            parables_easy = [q for q in parables_easy if q.get('id') != q_id]
        elif filename == 'medium.json':
            parables_medium = [q for q in parables_medium if q.get('id') != q_id]
        elif filename == 'hard.json':
            parables_hard = [q for q in parables_hard if q.get('id') != q_id]
        
        print(f"\n✅ Removed {q_id} from {filename}")
    
    # Save files
    with open('app/public/questions/parables-teachings/easy.json', 'w', encoding='utf-8') as f:
        json.dump(parables_easy, f, indent=2, ensure_ascii=False)
    
    with open('app/public/questions/parables-teachings/medium.json', 'w', encoding='utf-8') as f:
        json.dump(parables_medium, f, indent=2, ensure_ascii=False)
    
    with open('app/public/questions/parables-teachings/hard.json', 'w', encoding='utf-8') as f:
        json.dump(parables_hard, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Files saved!")
    
    # Update index
    with open('app/public/questions/index.json', 'r', encoding='utf-8') as f:
        index = json.load(f)
    
    for entry in index:
        if entry.get('themePath') == 'parables-teachings':
            if entry.get('difficulty') == 'easy':
                entry['count'] = len(parables_easy)
            elif entry.get('difficulty') == 'medium':
                entry['count'] = len(parables_medium)
            elif entry.get('difficulty') == 'hard':
                entry['count'] = len(parables_hard)
    
    with open('app/public/questions/index.json', 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Index updated!")
    print(f"\nNew counts:")
    print(f"  Easy: {len(parables_easy)}")
    print(f"  Medium: {len(parables_medium)}")
    print(f"  Hard: {len(parables_hard)}")
else:
    print("\n✅ No duplicates found!")
