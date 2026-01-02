import json

# Get existing questions to avoid duplicates
with open('app/public/questions/apostles/easy.json', 'r', encoding='utf-8') as f:
    existing = json.load(f)

existing_questions = {q['question'].lower() for q in existing}

# New easy questions to add - focusing on less-covered apostles and avoiding Peter, James, John, Paul
new_questions = [
    {
        "question": "Who replaced Judas Iscariot as the twelfth apostle?",
        "choices": ["Matthias", "Barnabas", "Timothy", "Silas"],
        "correctIndex": 0,
        "reference": {"book": "Acts", "chapter": 1, "verse": "26"},
        "explanation": "After Judas' betrayal and death, the apostles cast lots between Joseph called Barsabas and Matthias, and the lot fell to Matthias.",
        "verses": {"kjv": "And they gave forth their lots; and the lot fell upon Matthias; and he was numbered with the eleven apostles."}
    },
    {
        "question": "Which apostle was known as 'the Zealot'?",
        "choices": ["Simon", "Judas", "Matthew", "Thaddaeus"],
        "correctIndex": 0,
        "reference": {"book": "Luke", "chapter": 6, "verse": "15"},
        "explanation": "Simon the Zealot was one of the twelve apostles, distinguished from Simon Peter by this designation.",
        "verses": {"kjv": "Matthew and Thomas, James the son of Alphaeus, and Simon called Zelotes,"}
    },
    {
        "question": "What was the other name for the apostle Bartholomew?",
        "choices": ["Nathanael", "Thaddaeus", "Levi", "Barsabas"],
        "correctIndex": 0,
        "reference": {"book": "John", "chapter": 1, "verse": "45"},
        "explanation": "Bartholomew is generally identified with Nathanael, whom Philip brought to Jesus and who was from Cana of Galilee.",
        "verses": {"kjv": "Philip findeth Nathanael, and saith unto him, We have found him, of whom Moses in the law, and the prophets, did write, Jesus of Nazareth, the son of Joseph."}
    },
    {
        "question": "What was Matthew also called?",
        "choices": ["Levi", "Thaddaeus", "Judas", "Simon"],
        "correctIndex": 0,
        "reference": {"book": "Mark", "chapter": 2, "verse": "14"},
        "explanation": "The tax collector who became an apostle was known both as Matthew and as Levi, son of Alphaeus.",
        "verses": {"kjv": "And as he passed by, he saw Levi the son of Alphaeus sitting at the receipt of custom, and said unto him, Follow me. And he arose and followed him."}
    },
    {
        "question": "Which apostle brought Nathanael to Jesus?",
        "choices": ["Philip", "Andrew", "Matthew", "Bartholomew"],
        "correctIndex": 0,
        "reference": {"book": "John", "chapter": 1, "verse": "45"},
        "explanation": "Philip found Nathanael and told him they had found the one Moses and the prophets wrote about.",
        "verses": {"kjv": "Philip findeth Nathanael, and saith unto him, We have found him, of whom Moses in the law, and the prophets, did write, Jesus of Nazareth, the son of Joseph."}
    },
    {
        "question": "Which apostle said 'Can any good thing come out of Nazareth'?",
        "choices": ["Nathanael", "Thomas", "Philip", "Andrew"],
        "correctIndex": 0,
        "reference": {"book": "John", "chapter": 1, "verse": "46"},
        "explanation": "When Philip told Nathanael about Jesus of Nazareth, Nathanael skeptically asked if anything good could come from Nazareth.",
        "verses": {"kjv": "And Nathanael said unto him, Can there any good thing come out of Nazareth? Philip saith unto him, Come and see."}
    },
    {
        "question": "Which apostle is also called Judas, son of James?",
        "choices": ["Thaddaeus", "Matthew", "Bartholomew", "Simon"],
        "correctIndex": 0,
        "reference": {"book": "Luke", "chapter": 6, "verse": "16"},
        "explanation": "Thaddaeus is also known as Judas, son of James, and is sometimes called Lebbaeus to distinguish him from Judas Iscariot.",
        "verses": {"kjv": "And Judas the brother of James, and Judas Iscariot, which also was the traitor."}
    },
    {
        "question": "What did Nathanael call Jesus when he first met Him?",
        "choices": ["Son of God and King of Israel", "The Messiah", "Lord and Savior", "The Christ"],
        "correctIndex": 0,
        "reference": {"book": "John", "chapter": 1, "verse": "49"},
        "explanation": "After Jesus demonstrated His knowledge of Nathanael, Nathanael declared 'Rabbi, thou art the Son of God; thou art the King of Israel.'",
        "verses": {"kjv": "Nathanael answered and saith unto him, Rabbi, thou art the Son of God; thou art the King of Israel."}
    },
    {
        "question": "How many loaves and fishes did Andrew find for Jesus to multiply?",
        "choices": ["Five loaves and two fish", "Seven loaves and three fish", "Two loaves and five fish", "Three loaves and two fish"],
        "correctIndex": 0,
        "reference": {"book": "John", "chapter": 6, "verse": "9"},
        "explanation": "Andrew brought a boy with five barley loaves and two small fish to Jesus, who then multiplied them to feed the multitude.",
        "verses": {"kjv": "There is a lad here, which hath five barley loaves, and two small fishes: but what are they among so many?"}
    },
    {
        "question": "Which disciple questioned how they could know the way when Jesus said He was going away?",
        "choices": ["Thomas", "Philip", "Bartholomew", "Matthew"],
        "correctIndex": 0,
        "reference": {"book": "John", "chapter": 14, "verse": "5"},
        "explanation": "Thomas said to Jesus 'Lord, we know not whither thou goest; and how can we know the way?'",
        "verses": {"kjv": "Thomas saith unto him, Lord, we know not whither thou goest; and how can we know the way?"}
    },
    {
        "question": "What did the disciples do immediately after Jesus called them?",
        "choices": ["They left their nets and followed Him", "They finished their work first", "They went home to tell their families", "They asked for time to think"],
        "correctIndex": 0,
        "reference": {"book": "Matthew", "chapter": 4, "verse": "20"},
        "explanation": "When Jesus called the fishermen, they immediately left their nets and followed Him.",
        "verses": {"kjv": "And they straightway left their nets, and followed him."}
    },
    {
        "question": "Which apostle is listed last in most of the lists of the twelve?",
        "choices": ["Judas Iscariot", "Matthias", "Thaddaeus", "Simon the Zealot"],
        "correctIndex": 0,
        "reference": {"book": "Matthew", "chapter": 10, "verse": "4"},
        "explanation": "Judas Iscariot is consistently listed last among the twelve apostles, often identified as the one who betrayed Jesus.",
        "verses": {"kjv": "Simon the Canaanite, and Judas Iscariot, who also betrayed him."}
    },
    {
        "question": "How did Matthias become an apostle?",
        "choices": ["By casting lots", "By election", "Jesus appeared to him", "By drawing straws"],
        "correctIndex": 0,
        "reference": {"book": "Acts", "chapter": 1, "verse": "26"},
        "explanation": "The apostles prayed and cast lots between two candidates, and the lot fell to Matthias who was numbered with the eleven.",
        "verses": {"kjv": "And they gave forth their lots; and the lot fell upon Matthias; and he was numbered with the eleven apostles."}
    }
]

# Find available IDs
all_ids = {q['id'] for q in existing}
used_numbers = sorted([int(id.split('-')[-1]) for id in all_ids])

# Find gaps
available_ids = []
for i in range(1, 51):
    id_num = f"APO-E-{i:04d}"
    if id_num not in all_ids:
        available_ids.append(id_num)

print(f"Available IDs: {available_ids[:13]}")
print(f"Need {len(new_questions)} new questions")

# Assign IDs and add theme/difficulty
for i, q in enumerate(new_questions):
    q['id'] = available_ids[i]
    q['theme'] = 'Apostles'
    q['difficulty'] = 'easy'
    # Check for duplicates
    if q['question'].lower() in existing_questions:
        print(f"WARNING: Duplicate question: {q['question']}")

# Combine and sort
all_questions = existing + new_questions
all_questions.sort(key=lambda x: x['id'])

print(f"\nFinal count: {len(all_questions)}")

# Save
with open('app/public/questions/apostles/easy.json', 'w', encoding='utf-8') as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print("✓ Added 13 new questions and filled gaps")
