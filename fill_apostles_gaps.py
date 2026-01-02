import json

# Load existing files
with open('app/public/questions/apostles/easy.json', 'r', encoding='utf-8') as f:
    easy_questions = json.load(f)

with open('app/public/questions/apostles/medium.json', 'r', encoding='utf-8') as f:
    medium_questions = json.load(f)

# New EASY questions to fill gaps (APO-E-0031, 0032, 0033)
new_easy = [
    {
        "id": "APO-E-0031",
        "theme": "Apostles",
        "question": "What did Jesus command His disciples to do after His resurrection?",
        "choices": ["Go and make disciples of all nations", "Return to Galilee only", "Stay in Jerusalem forever", "Build a temple"],
        "correctIndex": 0,
        "difficulty": "easy",
        "reference": {"book": "Matthew", "chapter": 28, "verse": "19"},
        "explanation": "Jesus commanded the disciples to go and teach all nations, baptizing them in the name of the Father, Son, and Holy Ghost.",
        "verses": {"kjv": "Go ye therefore, and teach all nations, baptizing them in the name of the Father, and of the Son, and of the Holy Ghost:"}
    },
    {
        "id": "APO-E-0032",
        "theme": "Apostles",
        "question": "On which day of the week did the disciples meet when Jesus appeared to them after resurrection?",
        "choices": ["First day of the week", "Sabbath", "Third day", "Seventh day"],
        "correctIndex": 0,
        "difficulty": "easy",
        "reference": {"book": "John", "chapter": 20, "verse": "19"},
        "explanation": "On the first day of the week, the same day Jesus rose, He appeared to His disciples when they were assembled.",
        "verses": {"kjv": "Then the same day at evening, being the first day of the week, when the doors were shut where the disciples were assembled for fear of the Jews, came Jesus and stood in the midst, and saith unto them, Peace be unto you."}
    },
    {
        "id": "APO-E-0033",
        "theme": "Apostles",
        "question": "What did the apostles do after Jesus ascended into heaven?",
        "choices": ["Returned to Jerusalem with great joy", "Fled to Egypt", "Went fishing", "Hid in fear"],
        "correctIndex": 0,
        "difficulty": "easy",
        "reference": {"book": "Luke", "chapter": 24, "verse": "52"},
        "explanation": "After worshipping Jesus, the disciples returned to Jerusalem with great joy.",
        "verses": {"kjv": "And they worshipped him, and returned to Jerusalem with great joy:"}
    }
]

# New MEDIUM questions to fill gaps (APO-M-0028, 0029, 0033, 0050)
new_medium = [
    {
        "id": "APO-M-0028",
        "theme": "Apostles",
        "question": "Which apostle was known for bringing people to Jesus, including a boy with loaves and fish?",
        "choices": ["Andrew", "Philip", "Bartholomew", "Matthew"],
        "correctIndex": 0,
        "difficulty": "medium",
        "reference": {"book": "John", "chapter": 6, "verse": "8-9"},
        "explanation": "Andrew brought his brother Peter to Jesus, and later brought the boy with five loaves and two fish.",
        "verses": {"kjv": "One of his disciples, Andrew, Simon Peter's brother, saith unto him, There is a lad here, which hath five barley loaves, and two small fishes: but what are they among so many?"}
    },
    {
        "id": "APO-M-0029",
        "theme": "Apostles",
        "question": "Which Gospel records that Peter and another disciple ran to the tomb?",
        "choices": ["John", "Matthew", "Mark", "Luke"],
        "correctIndex": 0,
        "difficulty": "medium",
        "reference": {"book": "John", "chapter": 20, "verse": "3-4"},
        "explanation": "The Gospel of John records that Peter and John (the other disciple) ran together to the sepulchre.",
        "verses": {"kjv": "Peter therefore went forth, and that other disciple, and came to the sepulchre. So they ran both together: and the other disciple did outrun Peter, and came first to the sepulchre."}
    },
    {
        "id": "APO-M-0033",
        "theme": "Apostles",
        "question": "What did Jesus tell His disciples they would be after receiving the Holy Spirit?",
        "choices": ["Witnesses unto Him", "Kings and priests", "Prophets only", "Judges of Israel"],
        "correctIndex": 0,
        "difficulty": "medium",
        "reference": {"book": "Acts", "chapter": 1, "verse": "8"},
        "explanation": "Jesus told the disciples they would receive power when the Holy Ghost came upon them and be witnesses unto Him.",
        "verses": {"kjv": "But ye shall receive power, after that the Holy Ghost is come upon you: and ye shall be witnesses unto me both in Jerusalem, and in all Judaea, and in Samaria, and unto the uttermost part of the earth."}
    },
    {
        "id": "APO-M-0050",
        "theme": "Apostles",
        "question": "Where were the disciples when they received the Holy Spirit on Pentecost?",
        "choices": ["In an upper room in Jerusalem", "By the Sea of Galilee", "In the temple", "On Mount Sinai"],
        "correctIndex": 0,
        "difficulty": "medium",
        "reference": {"book": "Acts", "chapter": 2, "verse": "1-2"},
        "explanation": "The disciples were all with one accord in one place when the Holy Spirit came upon them on the day of Pentecost.",
        "verses": {"kjv": "And when the day of Pentecost was fully come, they were all with one accord in one place. And suddenly there came a sound from heaven as of a rushing mighty wind, and it filled all the house where they were sitting."}
    }
]

# Add new questions
easy_questions.extend(new_easy)
medium_questions.extend(new_medium)

# Sort by ID to maintain order
easy_questions.sort(key=lambda x: x['id'])
medium_questions.sort(key=lambda x: x['id'])

# Save updated files
with open('app/public/questions/apostles/easy.json', 'w', encoding='utf-8') as f:
    json.dump(easy_questions, f, indent=2, ensure_ascii=False)

with open('app/public/questions/apostles/medium.json', 'w', encoding='utf-8') as f:
    json.dump(medium_questions, f, indent=2, ensure_ascii=False)

print("✅ Successfully filled gaps in Apostles questions!")
print("   - Added 3 EASY questions (APO-E-0031, 0032, 0033)")
print("   - Added 4 MEDIUM questions (APO-M-0028, 0029, 0033, 0050)")
print("\n   Apostles theme should now be complete: 150 questions (50/50/50)")
