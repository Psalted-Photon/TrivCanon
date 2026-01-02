import json

# Load existing files
with open('app/public/questions/apostles/easy.json', 'r', encoding='utf-8') as f:
    easy_questions = json.load(f)

with open('app/public/questions/apostles/medium.json', 'r', encoding='utf-8') as f:
    medium_questions = json.load(f)

with open('app/public/questions/apostles/hard.json', 'r', encoding='utf-8') as f:
    hard_questions = json.load(f)

# New EASY questions (APO-E-0032 to APO-E-0050) - 19 questions
new_easy = [
    {
        "id": "APO-E-0032",
        "theme": "Apostles",
        "question": "How many apostles did Jesus choose?",
        "choices": ["Twelve", "Ten", "Seven", "Eleven"],
        "correctIndex": 0,
        "difficulty": "easy",
        "reference": {"book": "Mark", "chapter": 3, "verse": "14"},
        "explanation": "Jesus ordained twelve apostles to be with him and to preach.",
        "verses": {"kjv": "And he ordained twelve, that they should be with him, and that he might send them forth to preach,"}
    },
    {
        "id": "APO-E-0033",
        "theme": "Apostles",
        "question": "Which apostle walked on water with Jesus?",
        "choices": ["Peter", "John", "James", "Andrew"],
        "correctIndex": 0,
        "difficulty": "easy",
        "reference": {"book": "Matthew", "chapter": 14, "verse": "29"},
        "explanation": "Peter walked on the water toward Jesus, though he began to sink when he doubted.",
        "verses": {"kjv": "And he said, Come. And when Peter was come down out of the ship, he walked on the water, to go to Jesus."}
    },
    {
        "id": "APO-E-0034",
        "theme": "Apostles",
        "question": "Which apostle betrayed Jesus?",
        "choices": ["Judas Iscariot", "Peter", "Thomas", "Philip"],
        "correctIndex": 0,
        "difficulty": "easy",
        "reference": {"book": "Matthew", "chapter": 26, "verse": "14-15"},
        "explanation": "Judas Iscariot went to the chief priests and betrayed Jesus for thirty pieces of silver.",
        "verses": {"kjv": "Then one of the twelve, called Judas Iscariot, went unto the chief priests, And said unto them, What will ye give me, and I will deliver him unto you? And they covenanted with him for thirty pieces of silver."}
    },
    {
        "id": "APO-E-0035",
        "theme": "Apostles",
        "question": "Which apostle denied Jesus three times?",
        "choices": ["Peter", "Thomas", "Judas", "Matthew"],
        "correctIndex": 0,
        "difficulty": "easy",
        "reference": {"book": "Matthew", "chapter": 26, "verse": "75"},
        "explanation": "Peter denied knowing Jesus three times before the rooster crowed, just as Jesus had predicted.",
        "verses": {"kjv": "And Peter remembered the word of Jesus, which said unto him, Before the cock crow, thou shalt deny me thrice. And he went out, and wept bitterly."}
    },
    {
        "id": "APO-E-0036",
        "theme": "Apostles",
        "question": "What was Simon Peter doing when Jesus called him?",
        "choices": ["Fishing", "Collecting taxes", "Building", "Farming"],
        "correctIndex": 0,
        "difficulty": "easy",
        "reference": {"book": "Luke", "chapter": 5, "verse": "4-5"},
        "explanation": "Peter was washing his nets after fishing all night when Jesus told him to launch into the deep.",
        "verses": {"kjv": "Now when he had left speaking, he said unto Simon, Launch out into the deep, and let down your nets for a draught. And Simon answering said unto him, Master, we have toiled all the night, and have taken nothing: nevertheless at thy word I will let down the net."}
    },
    {
        "id": "APO-E-0037",
        "theme": "Apostles",
        "question": "Who was the brother of Simon Peter?",
        "choices": ["Andrew", "James", "John", "Philip"],
        "correctIndex": 0,
        "difficulty": "easy",
        "reference": {"book": "John", "chapter": 1, "verse": "40"},
        "explanation": "Andrew was Simon Peter's brother and one of the first disciples to follow Jesus.",
        "verses": {"kjv": "One of the two which heard John speak, and followed him, was Andrew, Simon Peter's brother."}
    },
    {
        "id": "APO-E-0038",
        "theme": "Apostles",
        "question": "Which disciple brought his brother to Jesus?",
        "choices": ["Andrew", "James", "Peter", "John"],
        "correctIndex": 0,
        "difficulty": "easy",
        "reference": {"book": "John", "chapter": 1, "verse": "41-42"},
        "explanation": "Andrew first found his brother Simon Peter and brought him to Jesus.",
        "verses": {"kjv": "He first findeth his own brother Simon, and saith unto him, We have found the Messias, which is, being interpreted, the Christ. And he brought him to Jesus."}
    },
    {
        "id": "APO-E-0039",
        "theme": "Apostles",
        "question": "What did Jesus promise to make Peter and Andrew?",
        "choices": ["Fishers of men", "Rulers of nations", "Teachers of law", "Builders of temples"],
        "correctIndex": 0,
        "difficulty": "easy",
        "reference": {"book": "Matthew", "chapter": 4, "verse": "19"},
        "explanation": "Jesus told them to follow Him and He would make them fishers of men.",
        "verses": {"kjv": "And he saith unto them, Follow me, and I will make you fishers of men."}
    },
    {
        "id": "APO-E-0040",
        "theme": "Apostles",
        "question": "Which apostle was present at the Transfiguration?",
        "choices": ["Peter", "Matthew", "Philip", "Bartholomew"],
        "correctIndex": 0,
        "difficulty": "easy",
        "reference": {"book": "Matthew", "chapter": 17, "verse": "1-2"},
        "explanation": "Peter, James, and John witnessed Jesus' transfiguration on the mountain.",
        "verses": {"kjv": "And after six days Jesus taketh Peter, James, and John his brother, and bringeth them up into an high mountain apart, And was transfigured before them: and his face did shine as the sun, and his raiment was white as the light."}
    },
    {
        "id": "APO-E-0041",
        "theme": "Apostles",
        "question": "Which apostle is known for his epistles in the New Testament?",
        "choices": ["Peter", "Philip", "Bartholomew", "Simon the Zealot"],
        "correctIndex": 0,
        "difficulty": "easy",
        "reference": {"book": "1 Peter", "chapter": 1, "verse": "1"},
        "explanation": "Peter wrote two epistles (1 Peter and 2 Peter) found in the New Testament.",
        "verses": {"kjv": "Peter, an apostle of Jesus Christ, to the strangers scattered throughout Pontus, Galatia, Cappadocia, Asia, and Bithynia,"}
    },
    {
        "id": "APO-E-0042",
        "theme": "Apostles",
        "question": "Which apostle wrote the Gospel that bears his name and three epistles?",
        "choices": ["John", "Matthew", "Peter", "James"],
        "correctIndex": 0,
        "difficulty": "easy",
        "reference": {"book": "John", "chapter": 21, "verse": "24"},
        "explanation": "John wrote the Gospel of John and the epistles 1 John, 2 John, and 3 John.",
        "verses": {"kjv": "This is the disciple which testifieth of these things, and wrote these things: and we know that his testimony is true."}
    },
    {
        "id": "APO-E-0043",
        "theme": "Apostles",
        "question": "Which apostle was the son of Zebedee?",
        "choices": ["James", "Peter", "Andrew", "Philip"],
        "correctIndex": 0,
        "difficulty": "easy",
        "reference": {"book": "Matthew", "chapter": 4, "verse": "21"},
        "explanation": "James and his brother John were the sons of Zebedee, called by Jesus while mending nets.",
        "verses": {"kjv": "And going on from thence, he saw other two brethren, James the son of Zebedee, and John his brother, in a ship with Zebedee their father, mending their nets; and he called them."}
    },
    {
        "id": "APO-E-0044",
        "theme": "Apostles",
        "question": "Who was called to follow Jesus while sitting at the tax office?",
        "choices": ["Matthew", "Luke", "Mark", "Zacchaeus"],
        "correctIndex": 0,
        "difficulty": "easy",
        "reference": {"book": "Mark", "chapter": 2, "verse": "14"},
        "explanation": "Matthew (Levi) was sitting at the receipt of custom when Jesus called him to follow.",
        "verses": {"kjv": "And as he passed by, he saw Levi the son of Alphaeus sitting at the receipt of custom, and said unto him, Follow me. And he arose and followed him."}
    },
    {
        "id": "APO-E-0045",
        "theme": "Apostles",
        "question": "Which apostle is called 'the beloved disciple' in the Gospel of John?",
        "choices": ["John", "Peter", "James", "Andrew"],
        "correctIndex": 0,
        "difficulty": "easy",
        "reference": {"book": "John", "chapter": 13, "verse": "23"},
        "explanation": "John is traditionally identified as the beloved disciple who leaned on Jesus' breast at the Last Supper.",
        "verses": {"kjv": "Now there was leaning on Jesus' bosom one of his disciples, whom Jesus loved."}
    },
    {
        "id": "APO-E-0046",
        "theme": "Apostles",
        "question": "How many pieces of silver did Judas receive for betraying Jesus?",
        "choices": ["Thirty", "Twenty", "Forty", "Fifty"],
        "correctIndex": 0,
        "difficulty": "easy",
        "reference": {"book": "Matthew", "chapter": 26, "verse": "15"},
        "explanation": "Judas received thirty pieces of silver from the chief priests for betraying Jesus.",
        "verses": {"kjv": "And said unto them, What will ye give me, and I will deliver him unto you? And they covenanted with him for thirty pieces of silver."}
    },
    {
        "id": "APO-E-0047",
        "theme": "Apostles",
        "question": "Which apostle cut off the ear of the high priest's servant?",
        "choices": ["Peter", "James", "John", "Andrew"],
        "correctIndex": 0,
        "difficulty": "easy",
        "reference": {"book": "John", "chapter": 18, "verse": "10"},
        "explanation": "Peter drew his sword and cut off the right ear of Malchus, the high priest's servant.",
        "verses": {"kjv": "Then Simon Peter having a sword drew it, and smote the high priest's servant, and cut off his right ear. The servant's name was Malchus."}
    },
    {
        "id": "APO-E-0048",
        "theme": "Apostles",
        "question": "Who was the first apostle to be martyred?",
        "choices": ["James", "Peter", "Paul", "Stephen"],
        "correctIndex": 0,
        "difficulty": "easy",
        "reference": {"book": "Acts", "chapter": 12, "verse": "2"},
        "explanation": "King Herod killed James, the brother of John, with the sword.",
        "verses": {"kjv": "And he killed James the brother of John with the sword."}
    },
    {
        "id": "APO-E-0049",
        "theme": "Apostles",
        "question": "Which apostle said to Jesus, 'Show us the Father'?",
        "choices": ["Philip", "Thomas", "Andrew", "Bartholomew"],
        "correctIndex": 0,
        "difficulty": "easy",
        "reference": {"book": "John", "chapter": 14, "verse": "8"},
        "explanation": "Philip asked Jesus to show them the Father, to which Jesus responded about knowing Him.",
        "verses": {"kjv": "Philip saith unto him, Lord, shew us the Father, and it sufficeth us."}
    },
    {
        "id": "APO-E-0050",
        "theme": "Apostles",
        "question": "What name did Jesus give to Simon?",
        "choices": ["Peter", "Rock", "Andrew", "James"],
        "correctIndex": 0,
        "difficulty": "easy",
        "reference": {"book": "John", "chapter": 1, "verse": "42"},
        "explanation": "Jesus gave Simon the name Cephas, which is translated as Peter, meaning rock.",
        "verses": {"kjv": "And he brought him to Jesus. And when Jesus beheld him, he said, Thou art Simon the son of Jona: thou shalt be called Cephas, which is by interpretation, A stone."}
    }
]

# New MEDIUM questions (APO-M-0030 to APO-M-0050) - 21 questions
new_medium = [
    {
        "id": "APO-M-0030",
        "theme": "Apostles",
        "question": "What was Peter's original name before Jesus renamed him?",
        "choices": ["Simon", "Simeon", "Samuel", "Saul"],
        "correctIndex": 0,
        "difficulty": "medium",
        "reference": {"book": "John", "chapter": 1, "verse": "42"},
        "explanation": "Peter was originally named Simon, son of Jona, before Jesus gave him the name Cephas (Peter).",
        "verses": {"kjv": "And he brought him to Jesus. And when Jesus beheld him, he said, Thou art Simon the son of Jona: thou shalt be called Cephas, which is by interpretation, A stone."}
    },
    {
        "id": "APO-M-0031",
        "theme": "Apostles",
        "question": "Which apostle was chosen to replace Judas Iscariot?",
        "choices": ["Matthias", "Barsabbas", "Paul", "Timothy"],
        "correctIndex": 0,
        "difficulty": "medium",
        "reference": {"book": "Acts", "chapter": 1, "verse": "26"},
        "explanation": "After casting lots, Matthias was chosen to replace Judas among the twelve apostles.",
        "verses": {"kjv": "And they gave forth their lots; and the lot fell upon Matthias; and he was numbered with the eleven apostles."}
    },
    {
        "id": "APO-M-0032",
        "theme": "Apostles",
        "question": "What was the occupation of James and John before following Jesus?",
        "choices": ["Fishermen", "Tax collectors", "Tentmakers", "Carpenters"],
        "correctIndex": 0,
        "difficulty": "medium",
        "reference": {"book": "Mark", "chapter": 1, "verse": "19-20"},
        "explanation": "James and John were fishermen, mending their nets with their father Zebedee when Jesus called them.",
        "verses": {"kjv": "And when he had gone a little farther thence, he saw James the son of Zebedee, and John his brother, who also were in the ship mending their nets. And straightway he called them: and they left their father Zebedee in the ship with the hired servants, and went after him."}
    },
    {
        "id": "APO-M-0033",
        "theme": "Apostles",
        "question": "Which apostle brought Nathanael to Jesus?",
        "choices": ["Philip", "Andrew", "Peter", "James"],
        "correctIndex": 0,
        "difficulty": "medium",
        "reference": {"book": "John", "chapter": 1, "verse": "45"},
        "explanation": "Philip found Nathanael and told him they had found the Messiah, bringing him to Jesus.",
        "verses": {"kjv": "Philip findeth Nathanael, and saith unto him, We have found him, of whom Moses in the law, and the prophets, did write, Jesus of Nazareth, the son of Joseph."}
    },
    {
        "id": "APO-M-0034",
        "theme": "Apostles",
        "question": "Who was the father of James and John?",
        "choices": ["Zebedee", "Alphaeus", "Jonah", "Zacharias"],
        "correctIndex": 0,
        "difficulty": "medium",
        "reference": {"book": "Matthew", "chapter": 4, "verse": "21"},
        "explanation": "James and John were the sons of Zebedee, who was also a fisherman.",
        "verses": {"kjv": "And going on from thence, he saw other two brethren, James the son of Zebedee, and John his brother, in a ship with Zebedee their father, mending their nets; and he called them."}
    },
    {
        "id": "APO-M-0035",
        "theme": "Apostles",
        "question": "What question did Thomas ask Jesus at the Last Supper?",
        "choices": ["How can we know the way?", "Who will betray you?", "Where are you going?", "When will you return?"],
        "correctIndex": 0,
        "difficulty": "medium",
        "reference": {"book": "John", "chapter": 14, "verse": "5"},
        "explanation": "Thomas said to Jesus that they did not know where He was going, so how could they know the way.",
        "verses": {"kjv": "Thomas saith unto him, Lord, we know not whither thou goest; and how can we know the way?"}
    },
    {
        "id": "APO-M-0036",
        "theme": "Apostles",
        "question": "Which apostle is also called Levi?",
        "choices": ["Matthew", "James", "Simon", "Judas"],
        "correctIndex": 0,
        "difficulty": "medium",
        "reference": {"book": "Mark", "chapter": 2, "verse": "14"},
        "explanation": "Matthew the tax collector was also known as Levi, the son of Alphaeus.",
        "verses": {"kjv": "And as he passed by, he saw Levi the son of Alphaeus sitting at the receipt of custom, and said unto him, Follow me. And he arose and followed him."}
    },
    {
        "id": "APO-M-0037",
        "theme": "Apostles",
        "question": "How did Judas Iscariot die according to the book of Acts?",
        "choices": ["He fell headlong and burst open", "He hanged himself", "He was stoned", "He was crucified"],
        "correctIndex": 0,
        "difficulty": "medium",
        "reference": {"book": "Acts", "chapter": 1, "verse": "18"},
        "explanation": "Acts records that Judas fell headlong and his bowels gushed out in the field he purchased.",
        "verses": {"kjv": "Now this man purchased a field with the reward of iniquity; and falling headlong, he burst asunder in the midst, and all his bowels gushed out."}
    },
    {
        "id": "APO-M-0038",
        "theme": "Apostles",
        "question": "What was the name of the high priest's servant whose ear Peter cut off?",
        "choices": ["Malchus", "Caiaphas", "Annas", "Alexander"],
        "correctIndex": 0,
        "difficulty": "medium",
        "reference": {"book": "John", "chapter": 18, "verse": "10"},
        "explanation": "The servant's name was Malchus, and Peter cut off his right ear.",
        "verses": {"kjv": "Then Simon Peter having a sword drew it, and smote the high priest's servant, and cut off his right ear. The servant's name was Malchus."}
    },
    {
        "id": "APO-M-0039",
        "theme": "Apostles",
        "question": "Which two apostles did Jesus send to prepare the Passover?",
        "choices": ["Peter and John", "James and John", "Peter and Andrew", "Philip and Bartholomew"],
        "correctIndex": 0,
        "difficulty": "medium",
        "reference": {"book": "Luke", "chapter": 22, "verse": "8"},
        "explanation": "Jesus sent Peter and John to prepare the Passover meal for the disciples.",
        "verses": {"kjv": "And he sent Peter and John, saying, Go and prepare us the passover, that we may eat."}
    },
    {
        "id": "APO-M-0040",
        "theme": "Apostles",
        "question": "What did Andrew tell his brother Simon about Jesus?",
        "choices": ["We have found the Messias", "This is the Son of God", "The kingdom is at hand", "Repent and be saved"],
        "correctIndex": 0,
        "difficulty": "medium",
        "reference": {"book": "John", "chapter": 1, "verse": "41"},
        "explanation": "Andrew first found his brother Simon and told him they had found the Messias, which is Christ.",
        "verses": {"kjv": "He first findeth his own brother Simon, and saith unto him, We have found the Messias, which is, being interpreted, the Christ."}
    },
    {
        "id": "APO-M-0041",
        "theme": "Apostles",
        "question": "Which apostle said 'Lord, show us the Father, and it sufficeth us'?",
        "choices": ["Philip", "Thomas", "Bartholomew", "Matthew"],
        "correctIndex": 0,
        "difficulty": "medium",
        "reference": {"book": "John", "chapter": 14, "verse": "8"},
        "explanation": "Philip requested that Jesus show them the Father, believing that would be sufficient.",
        "verses": {"kjv": "Philip saith unto him, Lord, shew us the Father, and it sufficeth us."}
    },
    {
        "id": "APO-M-0042",
        "theme": "Apostles",
        "question": "In which city was Peter when he received the vision of the sheet with unclean animals?",
        "choices": ["Joppa", "Jerusalem", "Caesarea", "Antioch"],
        "correctIndex": 0,
        "difficulty": "medium",
        "reference": {"book": "Acts", "chapter": 10, "verse": "9-10"},
        "explanation": "Peter was in Joppa, on a housetop praying, when he received the vision about clean and unclean animals.",
        "verses": {"kjv": "On the morrow, as they went on their journey, and drew nigh unto the city, Peter went up upon the housetop to pray about the sixth hour: And he became very hungry, and would have eaten: but while they made ready, he fell into a trance,"}
    },
    {
        "id": "APO-M-0043",
        "theme": "Apostles",
        "question": "Which apostle asked Jesus about the man born blind, 'who sinned, this man or his parents'?",
        "choices": ["The disciples", "John", "Peter", "Thomas"],
        "correctIndex": 0,
        "difficulty": "medium",
        "reference": {"book": "John", "chapter": 9, "verse": "2"},
        "explanation": "The disciples asked Jesus whether the man or his parents had sinned, causing his blindness.",
        "verses": {"kjv": "And his disciples asked him, saying, Master, who did sin, this man, or his parents, that he was born blind?"}
    },
    {
        "id": "APO-M-0044",
        "theme": "Apostles",
        "question": "What was Peter doing on the night he had the vision about the sheet?",
        "choices": ["Praying on a housetop", "Fishing", "Walking by the sea", "Teaching in the temple"],
        "correctIndex": 0,
        "difficulty": "medium",
        "reference": {"book": "Acts", "chapter": 10, "verse": "9"},
        "explanation": "Peter went up on the housetop to pray about the sixth hour when he fell into a trance.",
        "verses": {"kjv": "On the morrow, as they went on their journey, and drew nigh unto the city, Peter went up upon the housetop to pray about the sixth hour:"}
    },
    {
        "id": "APO-M-0045",
        "theme": "Apostles",
        "question": "Which apostle was also known as Didymus?",
        "choices": ["Thomas", "James", "Judas", "Simon"],
        "correctIndex": 0,
        "difficulty": "medium",
        "reference": {"book": "John", "chapter": 11, "verse": "16"},
        "explanation": "Thomas was called Didymus, which means 'twin' in Greek.",
        "verses": {"kjv": "Then said Thomas, which is called Didymus, unto his fellowdisciples, Let us also go, that we may die with him."}
    },
    {
        "id": "APO-M-0046",
        "theme": "Apostles",
        "question": "Who questioned how 5,000 people could be fed in the wilderness?",
        "choices": ["Philip", "Andrew", "Peter", "John"],
        "correctIndex": 0,
        "difficulty": "medium",
        "reference": {"book": "John", "chapter": 6, "verse": "7"},
        "explanation": "Philip answered Jesus saying that two hundred pennyworth of bread would not be sufficient for them.",
        "verses": {"kjv": "Philip answered him, Two hundred pennyworth of bread is not sufficient for them, that every one of them may take a little."}
    },
    {
        "id": "APO-M-0047",
        "theme": "Apostles",
        "question": "Which apostle found the boy with five loaves and two fish?",
        "choices": ["Andrew", "Philip", "Peter", "John"],
        "correctIndex": 0,
        "difficulty": "medium",
        "reference": {"book": "John", "chapter": 6, "verse": "8-9"},
        "explanation": "Andrew, Simon Peter's brother, told Jesus about the lad with five barley loaves and two small fishes.",
        "verses": {"kjv": "One of his disciples, Andrew, Simon Peter's brother, saith unto him, There is a lad here, which hath five barley loaves, and two small fishes: but what are they among so many?"}
    },
    {
        "id": "APO-M-0048",
        "theme": "Apostles",
        "question": "How many days after the resurrection did Jesus appear to Thomas?",
        "choices": ["Eight days", "Three days", "Seven days", "Ten days"],
        "correctIndex": 0,
        "difficulty": "medium",
        "reference": {"book": "John", "chapter": 20, "verse": "26"},
        "explanation": "After eight days, Jesus appeared again to the disciples when Thomas was present.",
        "verses": {"kjv": "And after eight days again his disciples were within, and Thomas with them: then came Jesus, the doors being shut, and stood in the midst, and said, Peace be unto you."}
    },
    {
        "id": "APO-M-0049",
        "theme": "Apostles",
        "question": "What did Peter tell the lame beggar at the temple gate?",
        "choices": ["Silver and gold have I none", "Arise and walk", "Thy faith hath made thee whole", "Go in peace"],
        "correctIndex": 0,
        "difficulty": "medium",
        "reference": {"book": "Acts", "chapter": 3, "verse": "6"},
        "explanation": "Peter told the lame man that he had no silver or gold, but would give him what he had in Jesus' name.",
        "verses": {"kjv": "Then Peter said, Silver and gold have I none; but such as I have give I thee: In the name of Jesus Christ of Nazareth rise up and walk."}
    },
    {
        "id": "APO-M-0050",
        "theme": "Apostles",
        "question": "Which apostle was present when Jesus raised Jairus' daughter?",
        "choices": ["Peter", "Matthew", "Philip", "Andrew"],
        "correctIndex": 0,
        "difficulty": "medium",
        "reference": {"book": "Mark", "chapter": 5, "verse": "37"},
        "explanation": "Jesus allowed only Peter, James, and John to accompany Him when He raised Jairus' daughter.",
        "verses": {"kjv": "And he suffered no man to follow him, save Peter, and James, and John the brother of James."}
    }
]

# New HARD questions (APO-H-0020 to APO-H-0050) - 31 questions
new_hard = [
    {
        "id": "APO-H-0020",
        "theme": "Apostles",
        "question": "In which town was Peter staying when Cornelius sent for him?",
        "choices": ["Joppa", "Caesarea", "Antioch", "Lydda"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Acts", "chapter": 10, "verse": "5"},
        "explanation": "Cornelius was told to send men to Joppa to fetch Simon Peter, who was lodging with Simon the tanner.",
        "verses": {"kjv": "And now send men to Joppa, and call for one Simon, whose surname is Peter:"}
    },
    {
        "id": "APO-H-0021",
        "theme": "Apostles",
        "question": "What was the name of the tanner with whom Peter stayed in Joppa?",
        "choices": ["Simon", "John", "Philip", "James"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Acts", "chapter": 9, "verse": "43"},
        "explanation": "Peter stayed many days in Joppa with one Simon, a tanner.",
        "verses": {"kjv": "And it came to pass, that he tarried many days in Joppa with one Simon a tanner."}
    },
    {
        "id": "APO-H-0022",
        "theme": "Apostles",
        "question": "Who was the father of Judas Iscariot?",
        "choices": ["Simon", "Alphaeus", "Zebedee", "Jonah"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "John", "chapter": 6, "verse": "71"},
        "explanation": "Judas Iscariot was the son of Simon, who would betray Jesus.",
        "verses": {"kjv": "He spake of Judas Iscariot the son of Simon: for he it was that should betray him, being one of the twelve."}
    },
    {
        "id": "APO-H-0023",
        "theme": "Apostles",
        "question": "Which apostle is identified as the son of Alphaeus?",
        "choices": ["James the Less", "Matthew", "Judas", "Simon"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Mark", "chapter": 3, "verse": "18"},
        "explanation": "James the son of Alphaeus is listed among the twelve apostles, also called James the Less.",
        "verses": {"kjv": "And Andrew, and Philip, and Bartholomew, and Matthew, and Thomas, and James the son of Alphaeus, and Thaddaeus, and Simon the Canaanite,"}
    },
    {
        "id": "APO-H-0024",
        "theme": "Apostles",
        "question": "What other name is given for the apostle Thaddaeus?",
        "choices": ["Judas the brother of James", "Lebbaeus", "Simon Zelotes", "Bartholomew"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Luke", "chapter": 6, "verse": "16"},
        "explanation": "Thaddaeus is also identified as Judas the brother of James (not Iscariot).",
        "verses": {"kjv": "And Judas the brother of James, and Judas Iscariot, which also was the traitor."}
    },
    {
        "id": "APO-H-0025",
        "theme": "Apostles",
        "question": "In which town did Jesus find Philip?",
        "choices": ["Bethsaida", "Capernaum", "Nazareth", "Cana"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "John", "chapter": 1, "verse": "43-44"},
        "explanation": "Jesus found Philip in Bethsaida, the city of Andrew and Peter.",
        "verses": {"kjv": "The day following Jesus would go forth into Galilee, and findeth Philip, and saith unto him, Follow me. Now Philip was of Bethsaida, the city of Andrew and Peter."}
    },
    {
        "id": "APO-H-0026",
        "theme": "Apostles",
        "question": "What was Bartholomew's hometown according to tradition?",
        "choices": ["Cana", "Bethsaida", "Nazareth", "Capernaum"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "John", "chapter": 1, "verse": "45-46"},
        "explanation": "Nathanael (Bartholomew) was from Cana in Galilee, as indicated when Philip found him.",
        "verses": {"kjv": "Philip findeth Nathanael, and saith unto him, We have found him, of whom Moses in the law, and the prophets, did write, Jesus of Nazareth, the son of Joseph. And Nathanael said unto him, Can there any good thing come out of Nazareth? Philip saith unto him, Come and see."}
    },
    {
        "id": "APO-H-0027",
        "theme": "Apostles",
        "question": "Which king killed the apostle James with a sword?",
        "choices": ["Herod Agrippa I", "Herod Antipas", "Herod the Great", "Pontius Pilate"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Acts", "chapter": 12, "verse": "1-2"},
        "explanation": "Herod Agrippa I (called Herod the king) killed James the brother of John with the sword.",
        "verses": {"kjv": "Now about that time Herod the king stretched forth his hands to vex certain of the church. And he killed James the brother of John with the sword."}
    },
    {
        "id": "APO-H-0028",
        "theme": "Apostles",
        "question": "How many fish did the disciples catch when Jesus told them to cast their net on the right side?",
        "choices": ["153", "276", "120", "144"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "John", "chapter": 21, "verse": "11"},
        "explanation": "Simon Peter drew the net to land full of great fishes, one hundred and fifty-three.",
        "verses": {"kjv": "Simon Peter went up, and drew the net to land full of great fishes, an hundred and fifty and three: and for all there were so many, yet was not the net broken."}
    },
    {
        "id": "APO-H-0029",
        "theme": "Apostles",
        "question": "How many times did Jesus ask Peter if he loved Him after the resurrection?",
        "choices": ["Three", "Two", "Four", "Seven"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "John", "chapter": 21, "verse": "17"},
        "explanation": "Jesus asked Peter three times if he loved Him, corresponding to Peter's three denials.",
        "verses": {"kjv": "He saith unto him the third time, Simon, son of Jonas, lovest thou me? Peter was grieved because he said unto him the third time, Lovest thou me? And he said unto him, Lord, thou knowest all things; thou knowest that I love thee. Jesus saith unto him, Feed my sheep."}
    },
    {
        "id": "APO-H-0030",
        "theme": "Apostles",
        "question": "What was the field called that was bought with Judas' betrayal money?",
        "choices": ["Aceldama", "Gethsemane", "Kidron", "Golgotha"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Acts", "chapter": 1, "verse": "19"},
        "explanation": "The field purchased with the reward of iniquity was called Aceldama, meaning 'field of blood'.",
        "verses": {"kjv": "And it was known unto all the dwellers at Jerusalem; insomuch as that field is called in their proper tongue, Aceldama, that is to say, The field of blood."}
    },
    {
        "id": "APO-H-0031",
        "theme": "Apostles",
        "question": "Which two men were nominated to replace Judas as an apostle?",
        "choices": ["Joseph Barsabbas and Matthias", "Barnabas and Paul", "Silas and Timothy", "Stephen and Philip"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Acts", "chapter": 1, "verse": "23"},
        "explanation": "They appointed two men: Joseph called Barsabbas (surnamed Justus) and Matthias.",
        "verses": {"kjv": "And they appointed two, Joseph called Barsabas, who was surnamed Justus, and Matthias."}
    },
    {
        "id": "APO-H-0032",
        "theme": "Apostles",
        "question": "What was the surname of Joseph Barsabbas who was considered to replace Judas?",
        "choices": ["Justus", "Marcus", "Clement", "Rufus"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Acts", "chapter": 1, "verse": "23"},
        "explanation": "Joseph called Barsabbas was also surnamed Justus.",
        "verses": {"kjv": "And they appointed two, Joseph called Barsabas, who was surnamed Justus, and Matthias."}
    },
    {
        "id": "APO-H-0033",
        "theme": "Apostles",
        "question": "From where did Nathanael come when Philip found him?",
        "choices": ["Cana of Galilee", "Bethany", "Bethlehem", "Bethsaida"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "John", "chapter": 21, "verse": "2"},
        "explanation": "Nathanael of Cana in Galilee is mentioned among the disciples who went fishing.",
        "verses": {"kjv": "There were together Simon Peter, and Thomas called Didymus, and Nathanael of Cana in Galilee, and the sons of Zebedee, and two other of his disciples."}
    },
    {
        "id": "APO-H-0034",
        "theme": "Apostles",
        "question": "What was Matthew's other name mentioned in the Gospels?",
        "choices": ["Levi", "Alphaeus", "Thaddaeus", "Simon"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Luke", "chapter": 5, "verse": "27"},
        "explanation": "Matthew the tax collector was also called Levi, the son of Alphaeus.",
        "verses": {"kjv": "And after these things he went forth, and saw a publican, named Levi, sitting at the receipt of custom: and he said unto him, Follow me."}
    },
    {
        "id": "APO-H-0035",
        "theme": "Apostles",
        "question": "Which apostle is specifically called 'the Canaanite' or 'Zelotes'?",
        "choices": ["Simon", "Judas", "James", "Matthew"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Luke", "chapter": 6, "verse": "15"},
        "explanation": "Simon was called Zelotes, indicating he may have been part of the Zealot movement.",
        "verses": {"kjv": "Matthew and Thomas, James the son of Alphaeus, and Simon called Zelotes,"}
    },
    {
        "id": "APO-H-0036",
        "theme": "Apostles",
        "question": "How many people were gathered in the upper room when Matthias was chosen?",
        "choices": ["About 120", "About 500", "About 70", "The eleven"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Acts", "chapter": 1, "verse": "15"},
        "explanation": "Peter stood up among the disciples, numbering about one hundred and twenty.",
        "verses": {"kjv": "And in those days Peter stood up in the midst of the disciples, and said, (the number of names together were about an hundred and twenty,)"}
    },
    {
        "id": "APO-H-0037",
        "theme": "Apostles",
        "question": "What did Peter say would happen to him when he grew old?",
        "choices": ["Another would gird him and carry him where he would not", "He would see the kingdom of God", "He would deny Christ again", "He would be crowned with glory"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "John", "chapter": 21, "verse": "18"},
        "explanation": "Jesus told Peter that when he was old, another would gird him and carry him where he did not wish to go.",
        "verses": {"kjv": "Verily, verily, I say unto thee, When thou wast young, thou girdedst thyself, and walkedst whither thou wouldest: but when thou shalt be old, thou shalt stretch forth thy hands, and another shall gird thee, and carry thee whither thou wouldest not."}
    },
    {
        "id": "APO-H-0038",
        "theme": "Apostles",
        "question": "Who was the mother of James and John?",
        "choices": ["Salome", "Mary Magdalene", "Mary of Bethany", "Joanna"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Mark", "chapter": 15, "verse": "40"},
        "explanation": "Salome is traditionally identified as the mother of Zebedee's children (James and John).",
        "verses": {"kjv": "There were also women looking on afar off: among whom was Mary Magdalene, and Mary the mother of James the less and of Joses, and Salome;"}
    },
    {
        "id": "APO-H-0039",
        "theme": "Apostles",
        "question": "In which city did Peter heal Aeneas who had been bedridden for eight years?",
        "choices": ["Lydda", "Joppa", "Caesarea", "Samaria"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Acts", "chapter": 9, "verse": "32-33"},
        "explanation": "Peter came to the saints at Lydda and found Aeneas who had been bedridden eight years with palsy.",
        "verses": {"kjv": "And it came to pass, as Peter passed throughout all quarters, he came down also to the saints which dwelt at Lydda. And there he found a certain man named Aeneas, which had kept his bed eight years, and was sick of the palsy."}
    },
    {
        "id": "APO-H-0040",
        "theme": "Apostles",
        "question": "What was the name of the woman Peter raised from the dead in Joppa?",
        "choices": ["Tabitha", "Lydia", "Priscilla", "Dorcas"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Acts", "chapter": 9, "verse": "36"},
        "explanation": "Tabitha (also called Dorcas) was a disciple in Joppa who Peter raised from the dead.",
        "verses": {"kjv": "Now there was at Joppa a certain disciple named Tabitha, which by interpretation is called Dorcas: this woman was full of good works and almsdeeds which she did."}
    },
    {
        "id": "APO-H-0041",
        "theme": "Apostles",
        "question": "In which town was Tabitha (Dorcas) residing when she died?",
        "choices": ["Joppa", "Lydda", "Caesarea", "Jerusalem"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Acts", "chapter": 9, "verse": "36"},
        "explanation": "Tabitha was a disciple living in Joppa who became sick and died.",
        "verses": {"kjv": "Now there was at Joppa a certain disciple named Tabitha, which by interpretation is called Dorcas: this woman was full of good works and almsdeeds which she did."}
    },
    {
        "id": "APO-H-0042",
        "theme": "Apostles",
        "question": "Who was the centurion in Caesarea who sent for Peter?",
        "choices": ["Cornelius", "Julius", "Claudius", "Longinus"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Acts", "chapter": 10, "verse": "1"},
        "explanation": "Cornelius was a centurion of the Italian band in Caesarea who was devout and feared God.",
        "verses": {"kjv": "There was a certain man in Caesarea called Cornelius, a centurion of the band called the Italian band,"}
    },
    {
        "id": "APO-H-0043",
        "theme": "Apostles",
        "question": "What was the name of the Italian band to which Cornelius belonged?",
        "choices": ["The Italian band", "The Augustan band", "The Imperial band", "The Praetorian guard"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Acts", "chapter": 10, "verse": "1"},
        "explanation": "Cornelius was a centurion of the band called the Italian band.",
        "verses": {"kjv": "There was a certain man in Caesarea called Cornelius, a centurion of the band called the Italian band,"}
    },
    {
        "id": "APO-H-0044",
        "theme": "Apostles",
        "question": "At what hour did Cornelius see the angel in his vision?",
        "choices": ["The ninth hour", "The third hour", "The sixth hour", "The eleventh hour"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Acts", "chapter": 10, "verse": "3"},
        "explanation": "Cornelius saw clearly in a vision about the ninth hour of the day an angel of God coming to him.",
        "verses": {"kjv": "He saw in a vision evidently about the ninth hour of the day an angel of God coming in to him, and saying unto him, Cornelius."}
    },
    {
        "id": "APO-H-0045",
        "theme": "Apostles",
        "question": "What was Peter's vision about on the housetop in Joppa?",
        "choices": ["A sheet with clean and unclean animals", "A ladder to heaven", "A burning bush", "Seven golden lampstands"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Acts", "chapter": 10, "verse": "11-12"},
        "explanation": "Peter saw heaven opened and a vessel like a great sheet descending with all manner of beasts, creeping things, and fowls.",
        "verses": {"kjv": "And saw heaven opened, and a certain vessel descending unto him, as it had been a great sheet knit at the four corners, and let down to the earth: Wherein were all manner of fourfooted beasts of the earth, and wild beasts, and creeping things, and fowls of the air."}
    },
    {
        "id": "APO-H-0046",
        "theme": "Apostles",
        "question": "How many men did Cornelius send to Joppa to fetch Peter?",
        "choices": ["Three", "Two", "Four", "Five"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Acts", "chapter": 10, "verse": "7"},
        "explanation": "Cornelius called two of his household servants and a devout soldier, making three men total.",
        "verses": {"kjv": "And when the angel which spake unto Cornelius was departed, he called two of his household servants, and a devout soldier of them that waited on him continually;"}
    },
    {
        "id": "APO-H-0047",
        "theme": "Apostles",
        "question": "What did the voice tell Peter regarding the animals in the sheet?",
        "choices": ["Kill and eat", "Take and sacrifice", "Observe and learn", "Touch not"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Acts", "chapter": 10, "verse": "13"},
        "explanation": "A voice came to Peter saying, 'Rise, Peter; kill, and eat.'",
        "verses": {"kjv": "And there came a voice to him, Rise, Peter; kill, and eat."}
    },
    {
        "id": "APO-H-0048",
        "theme": "Apostles",
        "question": "How many times was the sheet with animals let down to Peter in his vision?",
        "choices": ["Three times", "Once", "Twice", "Seven times"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Acts", "chapter": 10, "verse": "16"},
        "explanation": "This was done three times, and the vessel was received up again into heaven.",
        "verses": {"kjv": "This was done thrice: and the vessel was received up again into heaven."}
    },
    {
        "id": "APO-H-0049",
        "theme": "Apostles",
        "question": "Which apostle suggested buying food for 5,000 people would cost 200 denarii?",
        "choices": ["Philip", "Andrew", "Peter", "Matthew"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "John", "chapter": 6, "verse": "7"},
        "explanation": "Philip calculated that two hundred pennyworth of bread would not be sufficient for each to have a little.",
        "verses": {"kjv": "Philip answered him, Two hundred pennyworth of bread is not sufficient for them, that every one of them may take a little."}
    },
    {
        "id": "APO-H-0050",
        "theme": "Apostles",
        "question": "What was the name of the gate where Peter and John healed the lame man?",
        "choices": ["Beautiful", "Golden", "Sheep", "Eastern"],
        "correctIndex": 0,
        "difficulty": "hard",
        "reference": {"book": "Acts", "chapter": 3, "verse": "2"},
        "explanation": "A lame man was laid daily at the gate of the temple called Beautiful to ask for alms.",
        "verses": {"kjv": "And a certain man lame from his mother's womb was carried, whom they laid daily at the gate of the temple which is called Beautiful, to ask alms of them that entered into the temple;"}
    }
]

# Add new questions to existing lists
easy_questions.extend(new_easy)
medium_questions.extend(new_medium)
hard_questions.extend(new_hard)

# Save updated files
with open('app/public/questions/apostles/easy.json', 'w', encoding='utf-8') as f:
    json.dump(easy_questions, f, indent=2, ensure_ascii=False)

with open('app/public/questions/apostles/medium.json', 'w', encoding='utf-8') as f:
    json.dump(medium_questions, f, indent=2, ensure_ascii=False)

with open('app/public/questions/apostles/hard.json', 'w', encoding='utf-8') as f:
    json.dump(hard_questions, f, indent=2, ensure_ascii=False)

print("✅ Successfully added 71 Apostles questions!")
print("   - 19 EASY questions (APO-E-0032 to APO-E-0050)")
print("   - 21 MEDIUM questions (APO-M-0030 to APO-M-0050)")
print("   - 31 HARD questions (APO-H-0020 to APO-H-0050)")
print("\n   Total Apostles questions now: 150 (50 easy, 50 medium, 50 hard)")
