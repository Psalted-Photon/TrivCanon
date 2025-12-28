import json
import os

# Define the new questions to add to each theme
new_questions = {
    "prophets": {
        "easy": [
            {
                "id": "PRO-E-0026",
                "theme": "Prophets",
                "question": "Which prophet confronted King Ahab about Naboth's vineyard?",
                "choices": ["Elijah", "Elisha", "Isaiah", "Jeremiah"],
                "correctIndex": 0,
                "difficulty": "easy",
                "reference": {"book": "1 Kings", "chapter": 21, "verse": "17-19"},
                "explanation": "Elijah confronted Ahab for murdering Naboth and seizing his vineyard, prophesying judgment against him."
            },
            {
                "id": "PRO-E-0027",
                "theme": "Prophets",
                "question": "Which prophet anointed Saul as the first king of Israel?",
                "choices": ["Samuel", "Nathan", "Elijah", "Elisha"],
                "correctIndex": 0,
                "difficulty": "easy",
                "reference": {"book": "1 Samuel", "chapter": 10, "verse": "1"},
                "explanation": "Samuel took a flask of oil and poured it on Saul's head and kissed him, saying the Lord has anointed you leader over his inheritance."
            }
        ],
        "medium": [
            {
                "id": "PRO-M-0028",
                "theme": "Prophets",
                "question": "Which prophet was told to marry a prostitute as a sign to Israel?",
                "choices": ["Hosea", "Ezekiel", "Jeremiah", "Amos"],
                "correctIndex": 0,
                "difficulty": "medium",
                "reference": {"book": "Hosea", "chapter": 1, "verse": "2"},
                "explanation": "The Lord said to Hosea, 'Go, marry a promiscuous woman' to illustrate Israel's unfaithfulness to God."
            }
        ],
        "hard": [
            {
                "id": "PRO-H-0028",
                "theme": "Prophets",
                "question": "Which prophet saw a vision of a plumb line being used to test Israel?",
                "choices": ["Amos", "Zechariah", "Haggai", "Malachi"],
                "correctIndex": 0,
                "difficulty": "hard",
                "reference": {"book": "Amos", "chapter": 7, "verse": "7-8"},
                "explanation": "The Lord showed Amos a plumb line and said he would test Israel and no longer spare them."
            }
        ]
    },
    "apostles": {
        "easy": [
            {
                "id": "APO-E-0026",
                "theme": "Apostles",
                "question": "Which apostle was called 'the disciple whom Jesus loved'?",
                "choices": ["John", "Peter", "James", "Andrew"],
                "correctIndex": 0,
                "difficulty": "easy",
                "reference": {"book": "John", "chapter": 13, "verse": "23"},
                "explanation": "One of them, the disciple whom Jesus loved, was reclining next to him."
            },
            {
                "id": "APO-E-0027",
                "theme": "Apostles",
                "question": "Which apostle walked on water with Jesus?",
                "choices": ["Peter", "John", "Andrew", "James"],
                "correctIndex": 0,
                "difficulty": "easy",
                "reference": {"book": "Matthew", "chapter": 14, "verse": "29"},
                "explanation": "Peter got down out of the boat, walked on the water and came toward Jesus."
            }
        ],
        "medium": [
            {
                "id": "APO-M-0026",
                "theme": "Apostles",
                "question": "Which two apostles were sent by Jesus to prepare the Passover meal?",
                "choices": ["Peter and John", "James and John", "Peter and Andrew", "Philip and Bartholomew"],
                "correctIndex": 0,
                "difficulty": "medium",
                "reference": {"book": "Luke", "chapter": 22, "verse": "8"},
                "explanation": "Jesus sent Peter and John, saying, 'Go and make preparations for us to eat the Passover.'"
            },
            {
                "id": "APO-M-0027",
                "theme": "Apostles",
                "question": "Which apostle brought his brother to Jesus?",
                "choices": ["Andrew", "James", "Philip", "John"],
                "correctIndex": 0,
                "difficulty": "medium",
                "reference": {"book": "John", "chapter": 1, "verse": "40-42"},
                "explanation": "Andrew, Simon Peter's brother, was one of the two who heard John and followed Jesus. He first found his own brother Simon."
            }
        ],
        "hard": [
            {
                "id": "APO-H-0025",
                "theme": "Apostles",
                "question": "Which apostle was also called Didymus?",
                "choices": ["Thomas", "Bartholomew", "James the Less", "Thaddaeus"],
                "correctIndex": 0,
                "difficulty": "hard",
                "reference": {"book": "John", "chapter": 20, "verse": "24"},
                "explanation": "Now Thomas (also known as Didymus), one of the Twelve, was not with the disciples when Jesus came."
            },
            {
                "id": "APO-H-0026",
                "theme": "Apostles",
                "question": "Which apostle was from Bethsaida, the same town as Peter and Andrew?",
                "choices": ["Philip", "Nathanael", "Matthew", "Simon the Zealot"],
                "correctIndex": 0,
                "difficulty": "hard",
                "reference": {"book": "John", "chapter": 1, "verse": "44"},
                "explanation": "Philip, like Andrew and Peter, was from the town of Bethsaida."
            }
        ]
    },
    "kings-rulers": {
        "easy": [
            {
                "id": "KNG-E-0026",
                "theme": "Kings & Rulers",
                "question": "Which king asked God for wisdom instead of riches?",
                "choices": ["Solomon", "David", "Hezekiah", "Josiah"],
                "correctIndex": 0,
                "difficulty": "easy",
                "reference": {"book": "1 Kings", "chapter": 3, "verse": "9"},
                "explanation": "Solomon asked for a discerning heart to govern God's people and to distinguish between right and wrong."
            },
            {
                "id": "KNG-E-0027",
                "theme": "Kings & Rulers",
                "question": "Which king defeated Goliath before becoming king?",
                "choices": ["David", "Saul", "Solomon", "Asa"],
                "correctIndex": 0,
                "difficulty": "easy",
                "reference": {"book": "1 Samuel", "chapter": 17, "verse": "50"},
                "explanation": "David triumphed over the Philistine with a sling and a stone; without a sword in his hand he struck down the Philistine and killed him."
            }
        ],
        "medium": [
            {
                "id": "KNG-M-0027",
                "theme": "Kings & Rulers",
                "question": "Which king tore his robes when he heard the Book of the Law?",
                "choices": ["Josiah", "Hezekiah", "Jehoshaphat", "Asa"],
                "correctIndex": 0,
                "difficulty": "medium",
                "reference": {"book": "2 Kings", "chapter": 22, "verse": "11"},
                "explanation": "When King Josiah heard the words of the Book of the Law, he tore his robes in repentance."
            }
        ],
        "hard": [
            {
                "id": "KNG-H-0026",
                "theme": "Kings & Rulers",
                "question": "Which king of Israel reigned for only seven days before committing suicide?",
                "choices": ["Zimri", "Tibni", "Omri", "Elah"],
                "correctIndex": 0,
                "difficulty": "hard",
                "reference": {"book": "1 Kings", "chapter": 16, "verse": "15"},
                "explanation": "Zimri reigned in Tirzah seven days. When the army heard that Zimri had plotted against the king and murdered him, Zimri went into the citadel and set the palace on fire around him and died."
            }
        ]
    },
    "battles-conquests": {
        "easy": [
            {
                "id": "BAT-E-0026",
                "theme": "Battles & Conquests",
                "question": "What weapon did David use to defeat Goliath?",
                "choices": ["A sling and stone", "A sword", "A spear", "A bow and arrow"],
                "correctIndex": 0,
                "difficulty": "easy",
                "reference": {"book": "1 Samuel", "chapter": 17, "verse": "49-50"},
                "explanation": "David took a stone, slung it, and struck the Philistine on his forehead. The stone sank into his forehead, and he fell on his face to the ground."
            },
            {
                "id": "BAT-E-0027",
                "theme": "Battles & Conquests",
                "question": "Which city's walls fell down after the Israelites marched around it?",
                "choices": ["Jericho", "Ai", "Jerusalem", "Bethel"],
                "correctIndex": 0,
                "difficulty": "easy",
                "reference": {"book": "Joshua", "chapter": 6, "verse": "20"},
                "explanation": "When the trumpets sounded, the army shouted, and at the sound of the trumpet, when the men gave a loud shout, the wall collapsed."
            }
        ],
        "medium": [
            {
                "id": "BAT-M-0027",
                "theme": "Battles & Conquests",
                "question": "Which judge defeated the Midianites with only 300 men?",
                "choices": ["Gideon", "Samson", "Deborah", "Jephthah"],
                "correctIndex": 0,
                "difficulty": "medium",
                "reference": {"book": "Judges", "chapter": 7, "verse": "7"},
                "explanation": "The Lord said to Gideon, 'With the three hundred men that lapped I will save you and give the Midianites into your hands.'"
            }
        ],
        "hard": [
            {
                "id": "BAT-H-0026",
                "theme": "Battles & Conquests",
                "question": "In which valley did the sun stand still during Joshua's battle?",
                "choices": ["Aijalon", "Jezreel", "Elah", "Kidron"],
                "correctIndex": 0,
                "difficulty": "hard",
                "reference": {"book": "Joshua", "chapter": 10, "verse": "12"},
                "explanation": "Joshua said to the Lord, 'Sun, stand still over Gibeon, and you, moon, over the Valley of Aijalon.'"
            }
        ]
    },
    "parables-teachings": {
        "easy": [
            {
                "id": "PAR-E-0023",
                "theme": "Parables & Teachings",
                "question": "In the parable of the lost sheep, how many sheep did the shepherd have?",
                "choices": ["100", "50", "75", "99"],
                "correctIndex": 0,
                "difficulty": "easy",
                "reference": {"book": "Luke", "chapter": 15, "verse": "4"},
                "explanation": "Suppose one of you has a hundred sheep and loses one of them. Doesn't he leave the ninety-nine in the open country and go after the lost sheep until he finds it?"
            },
            {
                "id": "PAR-E-0024",
                "theme": "Parables & Teachings",
                "question": "What did Jesus say we cannot serve along with God?",
                "choices": ["Money", "Family", "Work", "Friends"],
                "correctIndex": 0,
                "difficulty": "easy",
                "reference": {"book": "Matthew", "chapter": 6, "verse": "24"},
                "explanation": "No one can serve two masters. Either you will hate the one and love the other, or you will be devoted to the one and despise the other. You cannot serve both God and money."
            },
            {
                "id": "PAR-E-0025",
                "theme": "Parables & Teachings",
                "question": "What did Jesus say is the greatest commandment?",
                "choices": ["Love the Lord your God", "Do not steal", "Honor your parents", "Keep the Sabbath"],
                "correctIndex": 0,
                "difficulty": "easy",
                "reference": {"book": "Matthew", "chapter": 22, "verse": "37-38"},
                "explanation": "Jesus replied: 'Love the Lord your God with all your heart and with all your soul and with all your mind. This is the first and greatest commandment.'"
            },
            {
                "id": "PAR-E-0026",
                "theme": "Parables & Teachings",
                "question": "What did Jesus say about those who mourn?",
                "choices": ["They will be comforted", "They will be blessed", "They will find peace", "They will be saved"],
                "correctIndex": 0,
                "difficulty": "easy",
                "reference": {"book": "Matthew", "chapter": 5, "verse": "4"},
                "explanation": "Blessed are those who mourn, for they will be comforted."
            },
            {
                "id": "PAR-E-0027",
                "theme": "Parables & Teachings",
                "question": "Where did Jesus say to store up treasures?",
                "choices": ["In heaven", "In the temple", "In your heart", "In good deeds"],
                "correctIndex": 0,
                "difficulty": "easy",
                "reference": {"book": "Matthew", "chapter": 6, "verse": "20"},
                "explanation": "But store up for yourselves treasures in heaven, where moths and vermin do not destroy, and where thieves do not break in and steal."
            }
        ],
        "medium": [
            {
                "id": "PAR-M-0023",
                "theme": "Parables & Teachings",
                "question": "In the parable of the ten virgins, how many were wise?",
                "choices": ["5", "3", "7", "2"],
                "correctIndex": 0,
                "difficulty": "medium",
                "reference": {"book": "Matthew", "chapter": 25, "verse": "2"},
                "explanation": "Five of them were foolish and five were wise."
            },
            {
                "id": "PAR-M-0024",
                "theme": "Parables & Teachings",
                "question": "In the parable of the talents, how many talents did the first servant receive?",
                "choices": ["5", "2", "1", "10"],
                "correctIndex": 0,
                "difficulty": "medium",
                "reference": {"book": "Matthew", "chapter": 25, "verse": "15"},
                "explanation": "To one he gave five bags of gold, to another two bags, and to another one bag, each according to his ability."
            },
            {
                "id": "PAR-M-0025",
                "theme": "Parables & Teachings",
                "question": "What did Jesus say the Kingdom of Heaven is like in terms of a seed?",
                "choices": ["A mustard seed", "A wheat seed", "A barley seed", "A fig seed"],
                "correctIndex": 0,
                "difficulty": "medium",
                "reference": {"book": "Matthew", "chapter": 13, "verse": "31"},
                "explanation": "The kingdom of heaven is like a mustard seed, which a man took and planted in his field. Though it is the smallest of all seeds, yet when it grows, it is the largest of garden plants."
            },
            {
                "id": "PAR-M-0026",
                "theme": "Parables & Teachings",
                "question": "In the parable of the wedding banquet, what happened to the guest without wedding clothes?",
                "choices": ["He was thrown out", "He was given clothes", "He was forgiven", "He was seated last"],
                "correctIndex": 0,
                "difficulty": "medium",
                "reference": {"book": "Matthew", "chapter": 22, "verse": "13"},
                "explanation": "Then the king told the attendants, 'Tie him hand and foot, and throw him outside, into the darkness, where there will be weeping and gnashing of teeth.'"
            },
            {
                "id": "PAR-M-0027",
                "theme": "Parables & Teachings",
                "question": "What did Jesus say about those who exalt themselves?",
                "choices": ["They will be humbled", "They will be punished", "They will be judged", "They will be rejected"],
                "correctIndex": 0,
                "difficulty": "medium",
                "reference": {"book": "Luke", "chapter": 14, "verse": "11"},
                "explanation": "For all those who exalt themselves will be humbled, and those who humble themselves will be exalted."
            }
        ],
        "hard": [
            {
                "id": "PAR-H-0022",
                "theme": "Parables & Teachings",
                "question": "In the parable of the shrewd manager, what did the manager do when he was about to be fired?",
                "choices": ["Reduced people's debts", "Stole money", "Quit immediately", "Begged for mercy"],
                "correctIndex": 0,
                "difficulty": "hard",
                "reference": {"book": "Luke", "chapter": 16, "verse": "5-7"},
                "explanation": "The manager called in his master's debtors and reduced their bills so they would take care of him after he lost his job."
            },
            {
                "id": "PAR-H-0023",
                "theme": "Parables & Teachings",
                "question": "In the parable of the persistent widow, what was she seeking from the judge?",
                "choices": ["Justice", "Money", "Property", "Freedom"],
                "correctIndex": 0,
                "difficulty": "hard",
                "reference": {"book": "Luke", "chapter": 18, "verse": "3"},
                "explanation": "And there was a widow in that town who kept coming to him with the plea, 'Grant me justice against my adversary.'"
            },
            {
                "id": "PAR-H-0024",
                "theme": "Parables & Teachings",
                "question": "In the parable of the rich fool, what did the man plan to do with his abundant crops?",
                "choices": ["Build bigger barns", "Give to the poor", "Sell them all", "Store them in the city"],
                "correctIndex": 0,
                "difficulty": "hard",
                "reference": {"book": "Luke", "chapter": 12, "verse": "18"},
                "explanation": "Then he said, 'This is what I'll do. I will tear down my barns and build bigger ones, and there I will store my surplus grain.'"
            },
            {
                "id": "PAR-H-0025",
                "theme": "Parables & Teachings",
                "question": "In the parable of the vineyard workers, when did the last workers start working?",
                "choices": ["The eleventh hour", "The ninth hour", "The sixth hour", "The third hour"],
                "correctIndex": 0,
                "difficulty": "hard",
                "reference": {"book": "Matthew", "chapter": 20, "verse": "6"},
                "explanation": "About five in the afternoon (the eleventh hour) he went out and found still others standing around."
            },
            {
                "id": "PAR-H-0026",
                "theme": "Parables & Teachings",
                "question": "What did the unmerciful servant owe his master in the parable?",
                "choices": ["Ten thousand talents", "One hundred denarii", "One talent", "Fifty talents"],
                "correctIndex": 0,
                "difficulty": "hard",
                "reference": {"book": "Matthew", "chapter": 18, "verse": "24"},
                "explanation": "As he began the settlement, a man who owed him ten thousand bags of gold was brought to him."
            }
        ]
    },
    "creation-origins": {
        "easy": [
            {
                "id": "CRE-E-0025",
                "theme": "Creation & Origins",
                "question": "On which day did God create the sun, moon, and stars?",
                "choices": ["Day 4", "Day 3", "Day 5", "Day 2"],
                "correctIndex": 0,
                "difficulty": "easy",
                "reference": {"book": "Genesis", "chapter": 1, "verse": "14-19"},
                "explanation": "And God said, 'Let there be lights in the vault of the sky to separate the day from the night.' This was the fourth day."
            },
            {
                "id": "CRE-E-0026",
                "theme": "Creation & Origins",
                "question": "What did God create on the fifth day?",
                "choices": ["Sea creatures and birds", "Land animals", "Plants", "Humans"],
                "correctIndex": 0,
                "difficulty": "easy",
                "reference": {"book": "Genesis", "chapter": 1, "verse": "20-23"},
                "explanation": "God created the great creatures of the sea and every living thing with which the water teems and every winged bird."
            },
            {
                "id": "CRE-E-0027",
                "theme": "Creation & Origins",
                "question": "What was the first thing God created?",
                "choices": ["Light", "Water", "Earth", "Heaven"],
                "correctIndex": 0,
                "difficulty": "easy",
                "reference": {"book": "Genesis", "chapter": 1, "verse": "3"},
                "explanation": "And God said, 'Let there be light,' and there was light. This was the first thing God created."
            }
        ],
        "medium": [
            {
                "id": "CRE-M-0025",
                "theme": "Creation & Origins",
                "question": "What was the name of the land where Cain went after killing Abel?",
                "choices": ["Nod", "Uz", "Havilah", "Shinar"],
                "correctIndex": 0,
                "difficulty": "medium",
                "reference": {"book": "Genesis", "chapter": 4, "verse": "16"},
                "explanation": "So Cain went out from the Lord's presence and lived in the land of Nod, east of Eden."
            },
            {
                "id": "CRE-M-0026",
                "theme": "Creation & Origins",
                "question": "Who was the father of all who play stringed instruments and pipes?",
                "choices": ["Jubal", "Tubal-Cain", "Jabal", "Lamech"],
                "correctIndex": 0,
                "difficulty": "medium",
                "reference": {"book": "Genesis", "chapter": 4, "verse": "21"},
                "explanation": "His brother's name was Jubal; he was the father of all who play stringed instruments and pipes."
            },
            {
                "id": "CRE-M-0027",
                "theme": "Creation & Origins",
                "question": "How old was Adam when Seth was born?",
                "choices": ["130 years", "100 years", "150 years", "120 years"],
                "correctIndex": 0,
                "difficulty": "medium",
                "reference": {"book": "Genesis", "chapter": 5, "verse": "3"},
                "explanation": "When Adam had lived 130 years, he had a son in his own likeness, in his own image; and he named him Seth."
            }
        ],
        "hard": [
            {
                "id": "CRE-H-0024",
                "theme": "Creation & Origins",
                "question": "Who was Enoch's son?",
                "choices": ["Methuselah", "Lamech", "Noah", "Jared"],
                "correctIndex": 0,
                "difficulty": "hard",
                "reference": {"book": "Genesis", "chapter": 5, "verse": "21"},
                "explanation": "When Enoch had lived 65 years, he became the father of Methuselah."
            },
            {
                "id": "CRE-H-0025",
                "theme": "Creation & Origins",
                "question": "How long did Enoch walk with God before he was taken up?",
                "choices": ["300 years", "365 years", "200 years", "500 years"],
                "correctIndex": 0,
                "difficulty": "hard",
                "reference": {"book": "Genesis", "chapter": 5, "verse": "22"},
                "explanation": "After he became the father of Methuselah, Enoch walked faithfully with God 300 years."
            },
            {
                "id": "CRE-H-0026",
                "theme": "Creation & Origins",
                "question": "What was the name of Cain's son?",
                "choices": ["Enoch", "Seth", "Lamech", "Irad"],
                "correctIndex": 0,
                "difficulty": "hard",
                "reference": {"book": "Genesis", "chapter": 4, "verse": "17"},
                "explanation": "Cain made love to his wife, and she became pregnant and gave birth to Enoch. Cain was then building a city, and he named it after his son Enoch."
            }
        ]
    },
    "prophecy-end-times": {
        "easy": [
            {
                "id": "END-E-0025",
                "theme": "Prophecy & End Times",
                "question": "According to Revelation, what will God wipe away from every eye?",
                "choices": ["Tears", "Sin", "Sadness", "Pain"],
                "correctIndex": 0,
                "difficulty": "easy",
                "reference": {"book": "Revelation", "chapter": 21, "verse": "4"},
                "explanation": "He will wipe every tear from their eyes. There will be no more death or mourning or crying or pain."
            },
            {
                "id": "END-E-0026",
                "theme": "Prophecy & End Times",
                "question": "What did Jesus say about the day and hour of His return?",
                "choices": ["No one knows", "The angels know", "The prophets know", "It is written"],
                "correctIndex": 0,
                "difficulty": "easy",
                "reference": {"book": "Matthew", "chapter": 24, "verse": "36"},
                "explanation": "But about that day or hour no one knows, not even the angels in heaven, nor the Son, but only the Father."
            },
            {
                "id": "END-E-0027",
                "theme": "Prophecy & End Times",
                "question": "What will happen to the earth and sky according to Revelation?",
                "choices": ["They will flee away", "They will be renewed", "They will be judged", "They will multiply"],
                "correctIndex": 0,
                "difficulty": "easy",
                "reference": {"book": "Revelation", "chapter": 20, "verse": "11"},
                "explanation": "Then I saw a great white throne and him who was seated on it. The earth and the heavens fled from his presence, and there was no place for them."
            }
        ],
        "medium": [
            {
                "id": "END-M-0026",
                "theme": "Prophecy & End Times",
                "question": "How many elders are around the throne in Revelation?",
                "choices": ["24", "12", "7", "70"],
                "correctIndex": 0,
                "difficulty": "medium",
                "reference": {"book": "Revelation", "chapter": 4, "verse": "4"},
                "explanation": "Surrounding the throne were twenty-four other thrones, and seated on them were twenty-four elders dressed in white."
            },
            {
                "id": "END-M-0027",
                "theme": "Prophecy & End Times",
                "question": "What are the names of the two witnesses in Revelation often associated with?",
                "choices": ["Two olive trees and two lampstands", "Two angels and two stars", "Two prophets and two kings", "Two mountains and two rivers"],
                "correctIndex": 0,
                "difficulty": "medium",
                "reference": {"book": "Revelation", "chapter": 11, "verse": "4"},
                "explanation": "They are the two olive trees and the two lampstands, and they stand before the Lord of the earth."
            }
        ],
        "hard": [
            {
                "id": "END-H-0025",
                "theme": "Prophecy & End Times",
                "question": "How long will the two witnesses prophesy in Revelation?",
                "choices": ["1,260 days", "42 months", "3.5 years", "1,000 days"],
                "correctIndex": 0,
                "difficulty": "hard",
                "reference": {"book": "Revelation", "chapter": 11, "verse": "3"},
                "explanation": "And I will appoint my two witnesses, and they will prophesy for 1,260 days, clothed in sackcloth."
            },
            {
                "id": "END-H-0026",
                "theme": "Prophecy & End Times",
                "question": "What is the name of the place where kings gather for battle in Revelation?",
                "choices": ["Armageddon", "Megiddo", "Babylon", "Gog"],
                "correctIndex": 0,
                "difficulty": "hard",
                "reference": {"book": "Revelation", "chapter": 16, "verse": "16"},
                "explanation": "Then they gathered the kings together to the place that in Hebrew is called Armageddon."
            }
        ]
    },
    "journeys-exile": {
        "easy": [
            {
                "id": "JRN-E-0025",
                "theme": "Journeys & Exile",
                "question": "Where did Moses lead the Israelites from?",
                "choices": ["Egypt", "Babylon", "Canaan", "Assyria"],
                "correctIndex": 0,
                "difficulty": "easy",
                "reference": {"book": "Exodus", "chapter": 12, "verse": "41"},
                "explanation": "At the end of the 430 years, to the very day, all the Lord's divisions left Egypt."
            },
            {
                "id": "JRN-E-0026",
                "theme": "Journeys & Exile",
                "question": "How many years did the Israelites wander in the wilderness?",
                "choices": ["40 years", "70 years", "400 years", "12 years"],
                "correctIndex": 0,
                "difficulty": "easy",
                "reference": {"book": "Numbers", "chapter": 14, "verse": "33"},
                "explanation": "Your children will be shepherds here for forty years, suffering for your unfaithfulness, until the last of your bodies lies in the wilderness."
            },
            {
                "id": "JRN-E-0027",
                "theme": "Journeys & Exile",
                "question": "Which sea did the Israelites cross when leaving Egypt?",
                "choices": ["Red Sea", "Dead Sea", "Mediterranean Sea", "Sea of Galilee"],
                "correctIndex": 0,
                "difficulty": "easy",
                "reference": {"book": "Exodus", "chapter": 14, "verse": "21-22"},
                "explanation": "Then Moses stretched out his hand over the sea, and the Lord drove the sea back and the Israelites went through the sea on dry ground."
            }
        ],
        "medium": [
            {
                "id": "JRN-M-0026",
                "theme": "Journeys & Exile",
                "question": "Which king took the Israelites into Babylonian exile?",
                "choices": ["Nebuchadnezzar", "Cyrus", "Sennacherib", "Xerxes"],
                "correctIndex": 0,
                "difficulty": "medium",
                "reference": {"book": "2 Kings", "chapter": 24, "verse": "14"},
                "explanation": "Nebuchadnezzar carried into exile all Jerusalem: all the officers and fighting men, and all the skilled workers and artisans."
            },
            {
                "id": "JRN-M-0027",
                "theme": "Journeys & Exile",
                "question": "How long did the Babylonian exile last?",
                "choices": ["70 years", "40 years", "50 years", "100 years"],
                "correctIndex": 0,
                "difficulty": "medium",
                "reference": {"book": "Jeremiah", "chapter": 29, "verse": "10"},
                "explanation": "When seventy years are completed for Babylon, I will come to you and fulfill my good promise to bring you back to this place."
            }
        ],
        "hard": [
            {
                "id": "JRN-H-0025",
                "theme": "Journeys & Exile",
                "question": "Which Persian king allowed the Jews to return from exile?",
                "choices": ["Cyrus", "Darius", "Xerxes", "Artaxerxes"],
                "correctIndex": 0,
                "difficulty": "hard",
                "reference": {"book": "Ezra", "chapter": 1, "verse": "1-2"},
                "explanation": "In the first year of Cyrus king of Persia, he issued a decree: The Lord has appointed me to build a temple for him at Jerusalem in Judah."
            },
            {
                "id": "JRN-H-0026",
                "theme": "Journeys & Exile",
                "question": "Who was the cupbearer to King Artaxerxes who rebuilt Jerusalem's walls?",
                "choices": ["Nehemiah", "Ezra", "Zerubbabel", "Haggai"],
                "correctIndex": 0,
                "difficulty": "hard",
                "reference": {"book": "Nehemiah", "chapter": 1, "verse": "11"},
                "explanation": "I was cupbearer to the king, and God granted him favor in the presence of the king to rebuild Jerusalem's walls."
            }
        ]
    },
    "festivals-customs": {
        "easy": [
            {
                "id": "FES-E-0026",
                "theme": "Festivals & Customs",
                "question": "What feast celebrates the harvest of first fruits?",
                "choices": ["Pentecost", "Passover", "Tabernacles", "Purim"],
                "correctIndex": 0,
                "difficulty": "easy",
                "reference": {"book": "Leviticus", "chapter": 23, "verse": "15-16"},
                "explanation": "Count off fifty days up to the day after the seventh Sabbath, and then present an offering of new grain to the Lord."
            },
            {
                "id": "FES-E-0027",
                "theme": "Festivals & Customs",
                "question": "On which day were the Israelites to do no work?",
                "choices": ["Sabbath", "Passover", "Day of Atonement", "All feast days"],
                "correctIndex": 0,
                "difficulty": "easy",
                "reference": {"book": "Exodus", "chapter": 20, "verse": "10"},
                "explanation": "But the seventh day is a sabbath to the Lord your God. On it you shall not do any work."
            }
        ],
        "medium": [
            {
                "id": "FES-M-0026",
                "theme": "Festivals & Customs",
                "question": "What was offered on the Day of Atonement?",
                "choices": ["Two goats", "A lamb", "A bull", "Seven rams"],
                "correctIndex": 0,
                "difficulty": "medium",
                "reference": {"book": "Leviticus", "chapter": 16, "verse": "7-8"},
                "explanation": "He is to take two goats and present them before the Lord. Aaron shall cast lots for the two goats—one lot for the Lord and the other for the scapegoat."
            },
            {
                "id": "FES-M-0027",
                "theme": "Festivals & Customs",
                "question": "How many days did the Feast of Unleavened Bread last?",
                "choices": ["7 days", "8 days", "3 days", "40 days"],
                "correctIndex": 0,
                "difficulty": "medium",
                "reference": {"book": "Exodus", "chapter": 12, "verse": "15"},
                "explanation": "For seven days you are to eat bread made without yeast. On the first day remove the yeast from your houses."
            }
        ],
        "hard": [
            {
                "id": "FES-H-0026",
                "theme": "Festivals & Customs",
                "question": "What was the name of the scapegoat on the Day of Atonement?",
                "choices": ["Azazel", "Baal", "Molech", "Dagon"],
                "correctIndex": 0,
                "difficulty": "hard",
                "reference": {"book": "Leviticus", "chapter": 16, "verse": "10"},
                "explanation": "But the goat chosen by lot as the scapegoat shall be presented alive before the Lord to be used for making atonement by sending it into the wilderness as a scapegoat to Azazel."
            }
        ]
    },
    "wisdom-psalms": {
        "easy": [
            {
                "id": "WIS-E-0025",
                "theme": "Wisdom & Psalms",
                "question": "Complete the verse: 'The Lord is my shepherd, I shall not...'",
                "choices": ["Want", "Fear", "Worry", "Stumble"],
                "correctIndex": 0,
                "difficulty": "easy",
                "reference": {"book": "Psalm", "chapter": 23, "verse": "1"},
                "explanation": "The Lord is my shepherd, I shall not want. This is one of the most famous verses in the Bible."
            },
            {
                "id": "WIS-E-0026",
                "theme": "Wisdom & Psalms",
                "question": "What is the beginning of wisdom according to Proverbs?",
                "choices": ["The fear of the Lord", "Understanding", "Knowledge", "Righteousness"],
                "correctIndex": 0,
                "difficulty": "easy",
                "reference": {"book": "Proverbs", "chapter": 9, "verse": "10"},
                "explanation": "The fear of the Lord is the beginning of wisdom, and knowledge of the Holy One is understanding."
            },
            {
                "id": "WIS-E-0027",
                "theme": "Wisdom & Psalms",
                "question": "According to Psalm 1, what is the blessed man NOT like?",
                "choices": ["Chaff", "A tree", "A rock", "A lion"],
                "correctIndex": 0,
                "difficulty": "easy",
                "reference": {"book": "Psalm", "chapter": 1, "verse": "4"},
                "explanation": "Not so the wicked! They are like chaff that the wind blows away."
            }
        ],
        "medium": [
            {
                "id": "WIS-M-0025",
                "theme": "Wisdom & Psalms",
                "question": "In Proverbs, what is more valuable than rubies?",
                "choices": ["Wisdom", "Gold", "Love", "Peace"],
                "correctIndex": 0,
                "difficulty": "medium",
                "reference": {"book": "Proverbs", "chapter": 8, "verse": "11"},
                "explanation": "For wisdom is more precious than rubies, and nothing you desire can compare with her."
            },
            {
                "id": "WIS-M-0026",
                "theme": "Wisdom & Psalms",
                "question": "What does Psalm 119:105 say God's word is?",
                "choices": ["A lamp to my feet", "A shield", "A sword", "A rock"],
                "correctIndex": 0,
                "difficulty": "medium",
                "reference": {"book": "Psalm", "chapter": 119, "verse": "105"},
                "explanation": "Your word is a lamp for my feet, a light on my path."
            },
            {
                "id": "WIS-M-0027",
                "theme": "Wisdom & Psalms",
                "question": "What does Proverbs say a gentle answer does?",
                "choices": ["Turns away wrath", "Brings wisdom", "Heals wounds", "Builds trust"],
                "correctIndex": 0,
                "difficulty": "medium",
                "reference": {"book": "Proverbs", "chapter": 15, "verse": "1"},
                "explanation": "A gentle answer turns away wrath, but a harsh word stirs up anger."
            }
        ],
        "hard": [
            {
                "id": "WIS-H-0024",
                "theme": "Wisdom & Psalms",
                "question": "What is the longest chapter in the Bible?",
                "choices": ["Psalm 119", "Psalm 23", "Genesis 1", "Isaiah 53"],
                "correctIndex": 0,
                "difficulty": "hard",
                "reference": {"book": "Psalm", "chapter": 119, "verse": "1"},
                "explanation": "Psalm 119 has 176 verses, making it the longest chapter in the Bible. It is an acrostic poem about God's law."
            },
            {
                "id": "WIS-H-0025",
                "theme": "Wisdom & Psalms",
                "question": "In Ecclesiastes, what does the Teacher say is meaningless?",
                "choices": ["Everything", "Wisdom", "Work", "Pleasure"],
                "correctIndex": 0,
                "difficulty": "hard",
                "reference": {"book": "Ecclesiastes", "chapter": 1, "verse": "2"},
                "explanation": "Meaningless! Meaningless! says the Teacher. Utterly meaningless! Everything is meaningless."
            },
            {
                "id": "WIS-H-0026",
                "theme": "Wisdom & Psalms",
                "question": "Who wrote most of the Proverbs?",
                "choices": ["Solomon", "David", "Moses", "Agur"],
                "correctIndex": 0,
                "difficulty": "hard",
                "reference": {"book": "Proverbs", "chapter": 1, "verse": "1"},
                "explanation": "The proverbs of Solomon son of David, king of Israel. Solomon wrote most of the book of Proverbs."
            }
        ]
    }
}

# Base path
base_path = "app/public/questions"

# Add questions to each file
for theme, difficulties in new_questions.items():
    for difficulty, questions in difficulties.items():
        file_path = os.path.join(base_path, theme, f"{difficulty}.json")
        
        # Read existing questions
        with open(file_path, 'r', encoding='utf-8') as f:
            existing_questions = json.load(f)
        
        # Add new questions
        existing_questions.extend(questions)
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(existing_questions, f, indent=2, ensure_ascii=False)
        
        print(f"Added {len(questions)} questions to {theme}/{difficulty}.json")

print("\n✅ All 70 questions added successfully!")
print("\nNew totals:")
print("Prophets: 80 (was 76)")
print("Apostles: 80 (was 74)")
print("Kings & Rulers: 80 (was 76)")
print("Battles & Conquests: 80 (was 76)")
print("Parables & Teachings: 80 (was 65)")
print("Creation & Origins: 80 (was 71)")
print("Prophecy & End Times: 80 (was 73)")
print("Journeys & Exile: 80 (was 73)")
print("Festivals & Customs: 80 (was 75)")
print("Wisdom & Psalms: 80 (was 71)")
print("\n🎉 Grand total: 960 questions (80 per theme × 12 themes)")
