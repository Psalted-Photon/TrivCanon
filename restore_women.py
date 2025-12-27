import json

# Load the Women of Faith questions
with open(r'C:\Users\Marlowe\Bible Trivia\women_of_faith_questions.json', 'r', encoding='utf-8') as f:
    women_questions = json.load(f)

# Load current cleaned file
with open(r'C:\Users\Marlowe\Bible Trivia\app\public\questions.json', 'r', encoding='utf-8') as f:
    current = json.load(f)

print(f"Loaded {len(women_questions)} Women of Faith questions")
print(f"Current file has {len(current)} questions")

# Check which Women of Faith questions are NOT duplicates of existing questions
existing_questions = {q['question'] for q in current}
unique_women = []
duplicate_women = []

for q in women_questions:
    if q['question'] not in existing_questions:
        unique_women.append(q)
    else:
        duplicate_women.append(q)

print(f"\nUnique Women of Faith questions to restore: {len(unique_women)}")
print(f"Women of Faith questions that are duplicates: {len(duplicate_women)}")

if duplicate_women:
    print("\nDuplicate Women of Faith questions:")
    for q in duplicate_women[:5]:
        print(f"  - {q['question']}")

# Add unique women questions back
combined = current + unique_women

# Renumber all questions
for i, q in enumerate(combined, 1):
    q['id'] = i

print(f"\nTotal after adding back: {len(combined)} questions")

# Save
with open(r'C:\Users\Marlowe\Bible Trivia\app\public\questions.json', 'w', encoding='utf-8') as f:
    json.dump(combined, f, indent=2, ensure_ascii=False)

print("File saved successfully!")

# Show theme distribution
from collections import Counter
themes = Counter(q['theme'] for q in combined)
print(f'\nTheme distribution:')
for theme, count in sorted(themes.items()):
    print(f'  {theme}: {count} questions')
