import json

# Read current file
with open('app/public/questions/wisdom-psalms/hard.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

print(f"Current count: {len(questions)} questions")

# New hard wisdom questions (WIS-H-0006 through WIS-H-0045)
new_questions = [
    {
        "id": "WIS-H-0006",
        "theme": "Wisdom & Psalms",
        "question": "In Job, who said 'The Lord gave, and the Lord hath taken away'?",
        "choices": ["Job", "Eliphaz", "Bildad", "Elihu"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Job", "chapter": 1, "verse": "21"},
        "explanation": "Job said, 'Naked came I out of my mother's womb, and naked shall I return thither: the Lord gave, and the Lord hath taken away; blessed be the name of the Lord.'"
    },
    {
        "id": "WIS-H-0007",
        "theme": "Wisdom & Psalms",
        "question": "Which psalm is known as the 'Shepherd Psalm'?",
        "choices": ["Psalm 23", "Psalm 100", "Psalm 1", "Psalm 51"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Psalm", "chapter": 23, "verse": "1"},
        "explanation": "Psalm 23 begins 'The Lord is my shepherd; I shall not want' and is one of the most beloved psalms."
    },
    {
        "id": "WIS-H-0008",
        "theme": "Wisdom & Psalms",
        "question": "According to Proverbs, what kind of words are like apples of gold in pictures of silver?",
        "choices": ["A word fitly spoken", "Kind words", "True words", "Wise words"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Proverbs", "chapter": 25, "verse": "11"},
        "explanation": "A word fitly spoken is like apples of gold in pictures of silver."
    },
    {
        "id": "WIS-H-0009",
        "theme": "Wisdom & Psalms",
        "question": "Which book of wisdom literature questions the justice of God's ways?",
        "choices": ["Job", "Ecclesiastes", "Proverbs", "Song of Solomon"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Job", "chapter": 1, "verse": "1"},
        "explanation": "The book of Job explores the problem of suffering and questions why the righteous suffer."
    },
    {
        "id": "WIS-H-0010",
        "theme": "Wisdom & Psalms",
        "question": "How many proverbs did Solomon speak according to 1 Kings?",
        "choices": ["3,000", "1,000", "5,000", "10,000"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "1 Kings", "chapter": 4, "verse": "32"},
        "explanation": "And he spake three thousand proverbs: and his songs were a thousand and five."
    },
    {
        "id": "WIS-H-0011",
        "theme": "Wisdom & Psalms",
        "question": "What does Ecclesiastes say is vanity of vanities?",
        "choices": ["All is vanity", "Riches", "Youth", "Wisdom"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Ecclesiastes", "chapter": 1, "verse": "2"},
        "explanation": "Vanity of vanities, saith the Preacher, vanity of vanities; all is vanity."
    },
    {
        "id": "WIS-H-0012",
        "theme": "Wisdom & Psalms",
        "question": "In Proverbs, what does a foolish son bring to his mother?",
        "choices": ["Heaviness", "Shame", "Grief", "Anger"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Proverbs", "chapter": 10, "verse": "1"},
        "explanation": "A wise son maketh a glad father: but a foolish son is the heaviness of his mother."
    },
    {
        "id": "WIS-H-0013",
        "theme": "Wisdom & Psalms",
        "question": "According to Psalm 90, what is the span of our years?",
        "choices": ["Threescore years and ten", "Fourscore years", "Fifty years", "One hundred years"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Psalm", "chapter": 90, "verse": "10"},
        "explanation": "The days of our years are threescore years and ten; and if by reason of strength they be fourscore years."
    },
    {
        "id": "WIS-H-0014",
        "theme": "Wisdom & Psalms",
        "question": "Which psalm begins 'Make a joyful noise unto the Lord'?",
        "choices": ["Psalm 100", "Psalm 95", "Psalm 98", "Psalm 150"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Psalm", "chapter": 100, "verse": "1"},
        "explanation": "Make a joyful noise unto the Lord, all ye lands."
    },
    {
        "id": "WIS-H-0015",
        "theme": "Wisdom & Psalms",
        "question": "In Job, what was the name of Job's oldest daughter?",
        "choices": ["Jemima", "Kezia", "Keren-happuch", "Dinah"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Job", "chapter": 42, "verse": "14"},
        "explanation": "And he called the name of the first, Jemima; and the name of the second, Kezia; and the name of the third, Keren-happuch."
    },
    {
        "id": "WIS-H-0016",
        "theme": "Wisdom & Psalms",
        "question": "According to Proverbs, the heart of the wise teaches what?",
        "choices": ["His mouth", "His hands", "His feet", "His eyes"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Proverbs", "chapter": 16, "verse": "23"},
        "explanation": "The heart of the wise teacheth his mouth, and addeth learning to his lips."
    },
    {
        "id": "WIS-H-0017",
        "theme": "Wisdom & Psalms",
        "question": "Which psalm is Moses's prayer?",
        "choices": ["Psalm 90", "Psalm 1", "Psalm 23", "Psalm 51"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Psalm", "chapter": 90, "verse": "1"},
        "explanation": "Psalm 90 is titled 'A Prayer of Moses the man of God.'"
    },
    {
        "id": "WIS-H-0018",
        "theme": "Wisdom & Psalms",
        "question": "In Song of Solomon, what is the beloved compared to among the daughters?",
        "choices": ["A lily among thorns", "A rose of Sharon", "A dove", "A fountain"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Song of Solomon", "chapter": 2, "verse": "2"},
        "explanation": "As the lily among thorns, so is my love among the daughters."
    },
    {
        "id": "WIS-H-0019",
        "theme": "Wisdom & Psalms",
        "question": "According to Ecclesiastes, what has God set in man's heart?",
        "choices": ["Eternity", "Love", "Wisdom", "Fear"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Ecclesiastes", "chapter": 3, "verse": "11"},
        "explanation": "He hath made every thing beautiful in his time: also he hath set the world (eternity) in their heart."
    },
    {
        "id": "WIS-H-0020",
        "theme": "Wisdom & Psalms",
        "question": "In Proverbs, a false balance is what to the Lord?",
        "choices": ["Abomination", "Sin", "Evil", "Wickedness"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Proverbs", "chapter": 11, "verse": "1"},
        "explanation": "A false balance is abomination to the Lord: but a just weight is his delight."
    },
    {
        "id": "WIS-H-0021",
        "theme": "Wisdom & Psalms",
        "question": "Which psalm contains the verse 'Deep calleth unto deep'?",
        "choices": ["Psalm 42", "Psalm 23", "Psalm 51", "Psalm 119"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Psalm", "chapter": 42, "verse": "7"},
        "explanation": "Deep calleth unto deep at the noise of thy waterspouts: all thy waves and thy billows are gone over me."
    },
    {
        "id": "WIS-H-0022",
        "theme": "Wisdom & Psalms",
        "question": "How many friends came to comfort Job?",
        "choices": ["Three", "Four", "Five", "Seven"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Job", "chapter": 2, "verse": "11"},
        "explanation": "Now when Job's three friends heard of all this evil that was come upon him, they came every one from his own place; Eliphaz the Temanite, and Bildad the Shuhite, and Zophar the Naamathite."
    },
    {
        "id": "WIS-H-0023",
        "theme": "Wisdom & Psalms",
        "question": "According to Proverbs, pride goes before what?",
        "choices": ["Destruction", "A fall", "Shame", "Dishonor"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Proverbs", "chapter": 16, "verse": "18"},
        "explanation": "Pride goeth before destruction, and an haughty spirit before a fall."
    },
    {
        "id": "WIS-H-0027",
        "theme": "Wisdom & Psalms",
        "question": "In Ecclesiastes, there is a time to be born and a time to what?",
        "choices": ["Die", "Live", "Weep", "Laugh"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Ecclesiastes", "chapter": 3, "verse": "2"},
        "explanation": "A time to be born, and a time to die; a time to plant, and a time to pluck up that which is planted."
    },
    {
        "id": "WIS-H-0028",
        "theme": "Wisdom & Psalms",
        "question": "Which psalm is David's psalm of repentance after his sin with Bathsheba?",
        "choices": ["Psalm 51", "Psalm 32", "Psalm 38", "Psalm 6"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Psalm", "chapter": 51, "verse": "1"},
        "explanation": "Psalm 51 is titled 'A Psalm of David, when Nathan the prophet came unto him, after he had gone in to Bathsheba.'"
    },
    {
        "id": "WIS-H-0029",
        "theme": "Wisdom & Psalms",
        "question": "According to Proverbs, what kind of rebuke is better than secret love?",
        "choices": ["Open rebuke", "Gentle rebuke", "Private rebuke", "Harsh rebuke"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Proverbs", "chapter": 27, "verse": "5"},
        "explanation": "Open rebuke is better than secret love."
    },
    {
        "id": "WIS-H-0030",
        "theme": "Wisdom & Psalms",
        "question": "In Job, what did God ask Job out of?",
        "choices": ["The whirlwind", "The fire", "The cloud", "The thunder"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Job", "chapter": 38, "verse": "1"},
        "explanation": "Then the Lord answered Job out of the whirlwind, and said, Who is this that darkeneth counsel by words without knowledge?"
    },
    {
        "id": "WIS-H-0031",
        "theme": "Wisdom & Psalms",
        "question": "According to Psalm 137, by which rivers did they sit down and weep?",
        "choices": ["Babylon", "Jordan", "Nile", "Euphrates"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Psalm", "chapter": 137, "verse": "1"},
        "explanation": "By the rivers of Babylon, there we sat down, yea, we wept, when we remembered Zion."
    },
    {
        "id": "WIS-H-0032",
        "theme": "Wisdom & Psalms",
        "question": "In Proverbs, what does a soft answer turn away?",
        "choices": ["Wrath", "Evil", "Sin", "Anger"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Proverbs", "chapter": 15, "verse": "1"},
        "explanation": "A soft answer turneth away wrath: but grievous words stir up anger."
    },
    {
        "id": "WIS-H-0033",
        "theme": "Wisdom & Psalms",
        "question": "Which psalm begins 'Bless the Lord, O my soul'?",
        "choices": ["Psalm 103", "Psalm 100", "Psalm 150", "Psalm 23"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Psalm", "chapter": 103, "verse": "1"},
        "explanation": "Bless the Lord, O my soul: and all that is within me, bless his holy name."
    },
    {
        "id": "WIS-H-0034",
        "theme": "Wisdom & Psalms",
        "question": "According to Ecclesiastes, what is there nothing new under?",
        "choices": ["The sun", "The heavens", "The earth", "The moon"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Ecclesiastes", "chapter": 1, "verse": "9"},
        "explanation": "The thing that hath been, it is that which shall be; and that which is done is that which shall be done: and there is no new thing under the sun."
    },
    {
        "id": "WIS-H-0035",
        "theme": "Wisdom & Psalms",
        "question": "In Job, how many sons did Job have before his trials?",
        "choices": ["Seven", "Three", "Ten", "Twelve"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Job", "chapter": 1, "verse": "2"},
        "explanation": "And there were born unto him seven sons and three daughters."
    },
    {
        "id": "WIS-H-0036",
        "theme": "Wisdom & Psalms",
        "question": "According to Proverbs, the fear of the Lord is the beginning of what?",
        "choices": ["Knowledge", "Wisdom", "Understanding", "Righteousness"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Proverbs", "chapter": 1, "verse": "7"},
        "explanation": "The fear of the Lord is the beginning of knowledge: but fools despise wisdom and instruction."
    },
    {
        "id": "WIS-H-0037",
        "theme": "Wisdom & Psalms",
        "question": "Which psalm contains 'The Lord reigneth; let the earth rejoice'?",
        "choices": ["Psalm 97", "Psalm 95", "Psalm 100", "Psalm 150"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Psalm", "chapter": 97, "verse": "1"},
        "explanation": "The Lord reigneth; let the earth rejoice; let the multitude of isles be glad thereof."
    },
    {
        "id": "WIS-H-0038",
        "theme": "Wisdom & Psalms",
        "question": "According to Proverbs, what kind of witness tells lies?",
        "choices": ["A false witness", "An unfaithful witness", "A wicked witness", "A deceitful witness"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Proverbs", "chapter": 14, "verse": "5"},
        "explanation": "A faithful witness will not lie: but a false witness will utter lies."
    },
    {
        "id": "WIS-H-0039",
        "theme": "Wisdom & Psalms",
        "question": "In Song of Solomon, where does the beloved say his love is like a roe or young hart?",
        "choices": ["Upon the mountains of Bether", "In the valleys", "By the fountains", "In the gardens"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Song of Solomon", "chapter": 2, "verse": "17"},
        "explanation": "Until the day break, and the shadows flee away, turn, my beloved, and be thou like a roe or a young hart upon the mountains of Bether."
    },
    {
        "id": "WIS-H-0040",
        "theme": "Wisdom & Psalms",
        "question": "According to Psalm 1, what is the blessed man like?",
        "choices": ["A tree planted by rivers of water", "A strong tower", "A solid rock", "A mighty fortress"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Psalm", "chapter": 1, "verse": "3"},
        "explanation": "And he shall be like a tree planted by the rivers of water, that bringeth forth his fruit in his season."
    },
    {
        "id": "WIS-H-0041",
        "theme": "Wisdom & Psalms",
        "question": "In Ecclesiastes, what did the Preacher say he hated?",
        "choices": ["Life", "Death", "Labor", "Vanity"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Ecclesiastes", "chapter": 2, "verse": "17"},
        "explanation": "Therefore I hated life; because the work that is wrought under the sun is grievous unto me: for all is vanity and vexation of spirit."
    },
    {
        "id": "WIS-H-0042",
        "theme": "Wisdom & Psalms",
        "question": "According to Proverbs, what covers all sins?",
        "choices": ["Love", "Faith", "Grace", "Mercy"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Proverbs", "chapter": 10, "verse": "12"},
        "explanation": "Hatred stirreth up strifes: but love covereth all sins."
    },
    {
        "id": "WIS-H-0043",
        "theme": "Wisdom & Psalms",
        "question": "Which psalm is the shortest psalm in the Bible?",
        "choices": ["Psalm 117", "Psalm 23", "Psalm 100", "Psalm 150"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Psalm", "chapter": 117, "verse": "1"},
        "explanation": "Psalm 117 has only two verses, making it the shortest psalm and the shortest chapter in the Bible."
    },
    {
        "id": "WIS-H-0044",
        "theme": "Wisdom & Psalms",
        "question": "In Job, what creature did God describe as 'chief of the ways of God'?",
        "choices": ["Behemoth", "Leviathan", "Dragon", "Lion"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Job", "chapter": 40, "verse": "19"},
        "explanation": "He is the chief of the ways of God: he that made him can make his sword to approach unto him."
    },
    {
        "id": "WIS-H-0045",
        "theme": "Wisdom & Psalms",
        "question": "According to Proverbs, where does a virtuous woman's price exceed?",
        "choices": ["Rubies", "Gold", "Silver", "Pearls"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Proverbs", "chapter": 31, "verse": "10"},
        "explanation": "Who can find a virtuous woman? for her price is far above rubies."
    }
]

# Add new questions
questions.extend(new_questions)

# Sort by ID
questions.sort(key=lambda q: q['id'])

# Write back
with open('app/public/questions/wisdom-psalms/hard.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)

print(f"✅ Added {len(new_questions)} new questions")
print(f"New total: {len(questions)} Wisdom & Psalms Hard questions")
