import json

# IDs to remove
ids_to_remove = [
    'APO-E-0010',  # Doubting Thomas duplicate
    'APO-E-0019',  # Doubting Thomas duplicate
    'APO-E-0023',  # Brother question duplicate
    'APO-E-0024',  # Doubting Thomas duplicate
    'APO-E-0025',  # Cutting ear duplicate
    'APO-E-0026',  # Peter fishing duplicate
    'APO-E-0029',  # Paul epistles duplicate
    'APO-E-0036',  # Peter fishing duplicate
    'APO-E-0037',  # Brother duplicate
    'APO-E-0038',  # Brother duplicate
    'APO-E-0040',  # Transfiguration duplicate
    'APO-E-0045',  # Beloved disciple duplicate
    'APO-E-0047',  # Cutting ear duplicate
]

# Load easy.json
with open('app/public/questions/apostles/easy.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

print(f"Original count: {len(questions)}")
print(f"Removing {len(ids_to_remove)} duplicate questions")

# Remove duplicates
filtered = [q for q in questions if q['id'] not in ids_to_remove]

print(f"New count: {len(filtered)}")
print(f"Removed: {len(questions) - len(filtered)}")

# Save back
with open('app/public/questions/apostles/easy.json', 'w', encoding='utf-8') as f:
    json.dump(filtered, f, indent=2, ensure_ascii=False)

print("\nRemoved IDs:")
for id in ids_to_remove:
    print(f"  - {id}")
