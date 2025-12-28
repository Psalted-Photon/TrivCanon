import json
import os

# Base path
base_path = "app/public/questions"
index_path = os.path.join(base_path, "index.json")

# Read current index
with open(index_path, 'r', encoding='utf-8') as f:
    index = json.load(f)

# Update counts based on actual file contents
for entry in index:
    theme_path = entry['themePath']
    difficulty = entry['difficulty']
    file_path = os.path.join(base_path, theme_path, f"{difficulty}.json")
    
    # Read the file and count questions
    with open(file_path, 'r', encoding='utf-8') as f:
        questions = json.load(f)
        actual_count = len(questions)
    
    # Update the count
    old_count = entry['count']
    entry['count'] = actual_count
    
    if old_count != actual_count:
        print(f"Updated {entry['theme']} {difficulty}: {old_count} → {actual_count}")

# Write updated index
with open(index_path, 'w', encoding='utf-8') as f:
    json.dump(index, f, indent=2, ensure_ascii=False)

print("\n✅ Index.json updated successfully!")
