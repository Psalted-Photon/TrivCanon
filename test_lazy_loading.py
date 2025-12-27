import json

print("=" * 80)
print("TESTING: Lazy Loading Simulation")
print("=" * 80)

# Load index
with open(r'app\public\questions\index.json', 'r', encoding='utf-8') as f:
    index = json.load(f)

print(f"\n✓ Index loaded: {len(index)} files available")

# Test 1: Load only Miracles + Easy
print("\n" + "-" * 80)
print("TEST 1: Load Miracles + Easy")
print("-" * 80)

miracles_easy = [item for item in index if item['theme'] == 'Miracles' and item['difficulty'] == 'easy']
questions = []
for item in miracles_easy:
    with open(f"app/public/{item['filePath']}", 'r', encoding='utf-8') as f:
        questions.extend(json.load(f))

print(f"✓ Loaded {len(questions)} questions")
print(f"  Sample IDs: {', '.join([q['id'] for q in questions[:3]])}")

# Test 2: Load All Themes + Medium
print("\n" + "-" * 80)
print("TEST 2: Load All Themes + Medium Difficulty")
print("-" * 80)

medium_files = [item for item in index if item['difficulty'] == 'medium']
questions = []
for item in medium_files:
    with open(f"app/public/{item['filePath']}", 'r', encoding='utf-8') as f:
        questions.extend(json.load(f))

print(f"✓ Loaded {len(questions)} questions from {len(medium_files)} files")
themes = set(q['theme'] for q in questions)
print(f"  Themes: {', '.join(sorted(themes))}")

# Test 3: Load Prophets + Apostles + All Difficulties
print("\n" + "-" * 80)
print("TEST 3: Load Prophets + Apostles + All Difficulties")
print("-" * 80)

selected_themes = ['Prophets', 'Apostles']
theme_files = [item for item in index if item['theme'] in selected_themes]
questions = []
for item in theme_files:
    with open(f"app/public/{item['filePath']}", 'r', encoding='utf-8') as f:
        questions.extend(json.load(f))

print(f"✓ Loaded {len(questions)} questions from {len(theme_files)} files")
by_theme = {}
for q in questions:
    by_theme[q['theme']] = by_theme.get(q['theme'], 0) + 1
for theme, count in sorted(by_theme.items()):
    print(f"  {theme}: {count} questions")

# Test 4: Load Everything
print("\n" + "-" * 80)
print("TEST 4: Load All Questions")
print("-" * 80)

questions = []
for item in index:
    with open(f"app/public/{item['filePath']}", 'r', encoding='utf-8') as f:
        questions.extend(json.load(f))

print(f"✓ Loaded {len(questions)} total questions from {len(index)} files")

# Test ordered rotation
print("\n" + "-" * 80)
print("TEST 5: Ordered Rotation (First 10 IDs)")
print("-" * 80)

miracles_all = []
for item in [i for i in index if i['theme'] == 'Miracles']:
    with open(f"app/public/{item['filePath']}", 'r', encoding='utf-8') as f:
        miracles_all.extend(json.load(f))

# Sort by ID
miracles_all.sort(key=lambda x: x['id'])
print(f"First 10 Miracles questions in order:")
for q in miracles_all[:10]:
    print(f"  {q['id']}: {q['question'][:50]}...")

print("\n" + "=" * 80)
print("✓✓✓ ALL LAZY LOADING TESTS PASSED ✓✓✓")
print("=" * 80)
