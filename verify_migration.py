import json
import os
from collections import defaultdict

print("=" * 80)
print("VERIFICATION: Question Migration Integrity Check")
print("=" * 80)

# Load index
with open(r'app\public\questions\index.json', 'r', encoding='utf-8') as f:
    index = json.load(f)

print(f"\n✓ Index loaded: {len(index)} files")

# Load all questions from new structure
all_questions = []
questions_by_file = {}

for item in index:
    file_path = f"app/public/{item['filePath']}"
    with open(file_path, 'r', encoding='utf-8') as f:
        questions = json.load(f)
    
    all_questions.extend(questions)
    questions_by_file[file_path] = len(questions)
    
    # Verify count matches index
    if len(questions) != item['count']:
        print(f"✗ MISMATCH: {file_path} has {len(questions)} but index says {item['count']}")
    else:
        print(f"✓ {item['theme']} - {item['difficulty']}: {len(questions)} questions")

# Load backup to compare
with open(r'app\public\questions-backup.json', 'r', encoding='utf-8') as f:
    backup_questions = json.load(f)

print(f"\n" + "=" * 80)
print("TOTALS")
print("=" * 80)
print(f"Backup file: {len(backup_questions)} questions")
print(f"New structure: {len(all_questions)} questions")
print(f"Difference: {len(all_questions) - len(backup_questions)}")

if len(all_questions) == len(backup_questions):
    print("✓ PASS: Question count matches!")
else:
    print("✗ FAIL: Question count mismatch!")

# Check for duplicate IDs
ids = [q['id'] for q in all_questions]
unique_ids = set(ids)

print(f"\nUnique IDs: {len(unique_ids)}")
if len(unique_ids) == len(ids):
    print("✓ PASS: No duplicate IDs")
else:
    print(f"✗ FAIL: {len(ids) - len(unique_ids)} duplicate IDs found!")

# Check ID format
valid_format = all(isinstance(q['id'], str) and '-' in q['id'] for q in all_questions)
if valid_format:
    print("✓ PASS: All IDs follow new format (THEME-DIFF-NUM)")
else:
    print("✗ FAIL: Some IDs don't follow new format")

# Verify all questions have required fields
required_fields = ['id', 'theme', 'question', 'choices', 'correctIndex', 'difficulty', 'reference', 'explanation']
missing_fields = []

for q in all_questions:
    for field in required_fields:
        if field not in q:
            missing_fields.append((q['id'], field))

if len(missing_fields) == 0:
    print("✓ PASS: All questions have required fields")
else:
    print(f"✗ FAIL: {len(missing_fields)} missing fields found")
    for qid, field in missing_fields[:5]:
        print(f"  - Question {qid} missing: {field}")

# Theme distribution
print(f"\n" + "=" * 80)
print("THEME DISTRIBUTION")
print("=" * 80)

theme_counts = defaultdict(int)
for q in all_questions:
    theme_counts[q['theme']] += 1

for theme, count in sorted(theme_counts.items()):
    print(f"{theme}: {count} questions")

# Difficulty distribution
print(f"\n" + "=" * 80)
print("DIFFICULTY DISTRIBUTION")
print("=" * 80)

diff_counts = defaultdict(int)
for q in all_questions:
    diff_counts[q['difficulty']] += 1

for diff, count in sorted(diff_counts.items()):
    print(f"{diff}: {count} questions")

print(f"\n" + "=" * 80)
print("FINAL VERDICT")
print("=" * 80)

all_pass = (
    len(all_questions) == len(backup_questions) and
    len(unique_ids) == len(ids) and
    valid_format and
    len(missing_fields) == 0
)

if all_pass:
    print("✓✓✓ ALL CHECKS PASSED ✓✓✓")
    print("Migration successful! Safe to remove old questions.json")
else:
    print("✗✗✗ SOME CHECKS FAILED ✗✗✗")
    print("DO NOT remove old questions.json until issues are resolved")
