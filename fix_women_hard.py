import json

# Load the file
with open('app/public/questions/women-of-faith/hard.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

print(f"Total questions before cleanup: {len(questions)}")

# Keep only the first 11 legitimate Women of Faith questions
# Questions 12-47 are all Parables & Teachings questions with wrong theme
correct_women_questions = questions[:11]

print(f"Keeping first 11 legitimate Women of Faith questions")
print(f"Removing {len(questions) - 11} misplaced Parables & Teachings questions")

# Save cleaned file
with open('app/public/questions/women-of-faith/hard.json', 'w', encoding='utf-8') as f:
    json.dump(correct_women_questions, f, indent=2, ensure_ascii=False)

print(f"\n✅ Fixed! New total: {len(correct_women_questions)} questions")

# Update index.json
with open('app/public/questions/index.json', 'r', encoding='utf-8') as f:
    index = json.load(f)

for entry in index:
    if entry.get('themePath') == 'women-of-faith' and entry.get('difficulty') == 'hard':
        entry['count'] = len(correct_women_questions)
        print(f"Updated index.json: women-of-faith/hard -> {len(correct_women_questions)} questions")

with open('app/public/questions/index.json', 'w', encoding='utf-8') as f:
    json.dump(index, f, indent=2, ensure_ascii=False)

print("\n✅ Index updated!")
