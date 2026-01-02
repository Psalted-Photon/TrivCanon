import json

# Load existing
with open('app/public/questions/women-of-faith/hard.json', 'r', encoding='utf-8') as f:
    existing = json.load(f)

print(f"Current count: {len(existing)}")
print(f"Last ID: {existing[-1]['id']}")

# These are the 39 legitimate Women of Faith questions
new_questions = [
  {
    "question": "What was the name of Naomi's daughter-in-law who chose to return to Moab?",
    "choices": ["Orpah", "Ruth", "Dinah", "Tamar"],
    "correctIndex": 0,
    "reference": {"book": "Ruth", "chapter": 1, "verse": "14"},
    "explanation": "Orpah kissed Naomi farewell and returned to her people, while Ruth clung to Naomi and continued to Bethlehem.",
    "verses": {"kjv": "And they lifted up their voice, and wept again: and Orpah kissed her mother in law; but Ruth clave unto her."}
  },
  {
    "question": "How many sons did Hannah have after Samuel?",
    "choices": ["Five more sons and two daughters", "Three sons", "One son", "Two sons and three daughters"],
    "correctIndex": 0,
    "reference": {"book": "1 Samuel", "chapter": 2, "verse": "21"},
    "explanation": "After giving Samuel to the Lord's service, Hannah was blessed with three more sons and two daughters.",
    "verses": {"kjv": "And the LORD visited Hannah, so that she conceived, and bare three sons and two daughters. And the child Samuel grew before the LORD."}
  },
  {
    "question": "What was the name of Abraham's concubine who bore Ishmael?",
    "choices": ["Hagar", "Bilhah", "Zilpah", "Keturah"],
    "correctIndex": 0,
    "reference": {"book": "Genesis", "chapter": 16, "verse": "15"},
    "explanation": "Hagar, Sarah's Egyptian maidservant, bore Ishmael to Abraham when Sarah was barren.",
    "verses": {"kjv": "And Hagar bare Abram a son: and Abram called his son's name, which Hagar bare, Ishmael."}
  },
  {
    "question": "Which prophetess was the wife of Shallum and advised King Josiah?",
    "choices": ["Huldah", "Deborah", "Miriam", "Anna"],
    "correctIndex": 0,
    "reference": {"book": "2 Kings", "chapter": 22, "verse": "14"},
    "explanation": "Huldah the prophetess verified the Book of the Law found in the temple during Josiah's reign.",
    "verses": {"kjv": "So Hilkiah the priest, and Ahikam, and Achbor, and Shaphan, and Asahiah, went unto Huldah the prophetess, the wife of Shallum the son of Tikvah, the son of Harhas, keeper of the wardrobe; (now she dwelt in Jerusalem in the college;) and they communed with her."}
  },
  {
    "question": "What did Jael use to kill Sisera?",
    "choices": ["A tent peg and hammer", "A sword", "A spear", "Poison"],
    "correctIndex": 0,
    "reference": {"book": "Judges", "chapter": 4, "verse": "21"},
    "explanation": "Jael took a tent peg and drove it through Sisera's temple with a hammer while he slept.",
    "verses": {"kjv": "Then Jael Heber's wife took a nail of the tent, and took an hammer in her hand, and went softly unto him, and smote the nail into his temples, and fastened it into the ground: for he was fast asleep and weary. So he died."}
  },
  {
    "question": "Which woman hid the spies on the roof with stalks of flax?",
    "choices": ["Rahab", "Tamar", "Abigail", "Esther"],
    "correctIndex": 0,
    "reference": {"book": "Joshua", "chapter": 2, "verse": "6"},
    "explanation": "Rahab hid the Israelite spies under stalks of flax on her roof before helping them escape from Jericho.",
    "verses": {"kjv": "But she had brought them up to the roof of the house, and hid them with the stalks of flax, which she had laid in order upon the roof."}
  },
  {
    "question": "What was the name of Boaz's first wife before Ruth?",
    "choices": ["The Bible doesn't mention a previous wife", "Naomi", "Orpah", "Tamar"],
    "correctIndex": 0,
    "reference": {"book": "Ruth", "chapter": 4, "verse": "13"},
    "explanation": "Scripture does not indicate Boaz had been married before Ruth; this was his marriage to Ruth as kinsman-redeemer.",
    "verses": {"kjv": "So Boaz took Ruth, and she was his wife: and when he went in unto her, the LORD gave her conception, and she bare a son."}
  },
  {
    "question": "How many handmaids did Leah give Jacob?",
    "choices": ["One (Zilpah)", "Two", "Three", "None"],
    "correctIndex": 0,
    "reference": {"book": "Genesis", "chapter": 30, "verse": "9"},
    "explanation": "When Leah ceased bearing, she gave her maid Zilpah to Jacob as a wife.",
    "verses": {"kjv": "When Leah saw that she had left bearing, she took Zilpah her maid, and gave her Jacob to wife."}
  },
  {
    "question": "Which woman's bones were carried out of Egypt during the Exodus?",
    "choices": ["No woman's bones are mentioned, only Joseph's", "Sarah", "Rachel", "Rebekah"],
    "correctIndex": 0,
    "reference": {"book": "Exodus", "chapter": 13, "verse": "19"},
    "explanation": "Moses took the bones of Joseph with him, as Joseph had made the children of Israel swear an oath.",
    "verses": {"kjv": "And Moses took the bones of Joseph with him: for he had straitly sworn the children of Israel, saying, God will surely visit you; and ye shall carry up my bones away hence with you."}
  },
  {
    "question": "What did Abigail bring to David to appease his anger?",
    "choices": ["Bread, wine, sheep, grain, raisins, and figs", "Gold and silver", "Livestock only", "Wine and oil"],
    "correctIndex": 0,
    "reference": {"book": "1 Samuel", "chapter": 25, "verse": "18"},
    "explanation": "Abigail quickly gathered a substantial provision to prevent David from taking vengeance on her foolish husband Nabal.",
    "verses": {"kjv": "Then Abigail made haste, and took two hundred loaves, and two bottles of wine, and five sheep ready dressed, and five measures of parched corn, and an hundred clusters of raisins, and two hundred cakes of figs, and laid them on asses."}
  },
  {
    "question": "What was the name of Michal's second husband after David?",
    "choices": ["Phaltiel (or Phalti)", "Adriel", "Ishbosheth", "Abner"],
    "correctIndex": 0,
    "reference": {"book": "2 Samuel", "chapter": 3, "verse": "15"},
    "explanation": "After Saul gave Michal to Phaltiel, David later demanded her return when he became king.",
    "verses": {"kjv": "And Ishbosheth sent, and took her from her husband, even from Phaltiel the son of Laish."}
  },
  {
    "question": "Which woman did King Ahasuerus depose before choosing Esther?",
    "choices": ["Vashti", "Zeresh", "Memucan", "Harbona"],
    "correctIndex": 0,
    "reference": {"book": "Esther", "chapter": 1, "verse": "19"},
    "explanation": "Queen Vashti was removed from her royal position for refusing to appear before the king and his guests.",
    "verses": {"kjv": "If it please the king, let there go a royal commandment from him, and let it be written among the laws of the Persians and the Medes, that it be not altered, That Vashti come no more before king Ahasuerus; and let the king give her royal estate unto another that is better than she."}
  },
  {
    "question": "How many years was the woman with the issue of blood afflicted?",
    "choices": ["Twelve years", "Seven years", "Eighteen years", "Ten years"],
    "correctIndex": 0,
    "reference": {"book": "Mark", "chapter": 5, "verse": "25"},
    "explanation": "The woman had suffered with a flow of blood for twelve years before touching Jesus' garment and being healed.",
    "verses": {"kjv": "And a certain woman, which had an issue of blood twelve years,"}
  },
  {
    "question": "What was Rebekah doing when Abraham's servant first saw her?",
    "choices": ["Drawing water from a well", "Tending sheep", "Grinding grain", "Weaving"],
    "correctIndex": 0,
    "reference": {"book": "Genesis", "chapter": 24, "verse": "15-16"},
    "explanation": "Rebekah came to the well with her pitcher and fulfilled the sign Abraham's servant had prayed for.",
    "verses": {"kjv": "And it came to pass, before he had done speaking, that, behold, Rebekah came out, who was born to Bethuel, son of Milcah, the wife of Nahor, Abraham's brother, with her pitcher upon her shoulder. And the damsel was very fair to look upon, a virgin, neither had any man known her: and she went down to the well, and filled her pitcher, and came up."}
  },
  {
    "question": "Which woman bargained with Jacob for mandrakes?",
    "choices": ["Leah", "Rachel", "Bilhah", "Zilpah"],
    "correctIndex": 0,
    "reference": {"book": "Genesis", "chapter": 30, "verse": "15-16"},
    "explanation": "Rachel wanted Reuben's mandrakes, so Leah traded them for a night with Jacob.",
    "verses": {"kjv": "And she said unto her, Is it a small matter that thou hast taken my husband? and wouldest thou take away my son's mandrakes also? And Rachel said, Therefore he shall lie with thee to night for thy son's mandrakes. And Jacob came out of the field in the evening, and Leah went out to meet him, and said, Thou must come in unto me; for surely I have hired thee with my son's mandrakes. And he lay with her that night."}
  },
  {
    "question": "What was the name of Job's wife?",
    "choices": ["The Bible does not record her name", "Dinah", "Zipporah", "Keturah"],
    "correctIndex": 0,
    "reference": {"book": "Job", "chapter": 2, "verse": "9"},
    "explanation": "Job's wife is mentioned but never named; she told Job to curse God and die.",
    "verses": {"kjv": "Then said his wife unto him, Dost thou still retain thine integrity? curse God, and die."}
  },
  {
    "question": "Which woman is mentioned as a seller of purple in Thyatira?",
    "choices": ["Lydia", "Priscilla", "Dorcas", "Phoebe"],
    "correctIndex": 0,
    "reference": {"book": "Acts", "chapter": 16, "verse": "14"},
    "explanation": "Lydia, a seller of purple goods from Thyatira, was converted and baptized with her household.",
    "verses": {"kjv": "And a certain woman named Lydia, a seller of purple, of the city of Thyatira, which worshipped God, heard us: whose heart the Lord opened, that she attended unto the things which were spoken of Paul."}
  },
  {
    "question": "How many daughters did Philip the evangelist have who prophesied?",
    "choices": ["Four", "Two", "Seven", "Three"],
    "correctIndex": 0,
    "reference": {"book": "Acts", "chapter": 21, "verse": "9"},
    "explanation": "Philip the evangelist had four unmarried daughters who all had the gift of prophecy.",
    "verses": {"kjv": "And the same man had four daughters, virgins, which did prophesy."}
  },
  {
    "question": "What did Rachel steal from her father Laban?",
    "choices": ["Household gods (teraphim)", "Gold", "Livestock", "Clothing"],
    "correctIndex": 0,
    "reference": {"book": "Genesis", "chapter": 31, "verse": "19"},
    "explanation": "Rachel stole her father's household idols when Jacob fled from Laban.",
    "verses": {"kjv": "And Laban went to shear his sheep: and Rachel had stolen the images that were her father's."}
  },
  {
    "question": "Which woman was the mother of Moses?",
    "choices": ["Jochebed", "Miriam", "Zipporah", "Puah"],
    "correctIndex": 0,
    "reference": {"book": "Exodus", "chapter": 6, "verse": "20"},
    "explanation": "Jochebed, the wife of Amram, gave birth to Moses, Aaron, and Miriam.",
    "verses": {"kjv": "And Amram took him Jochebed his father's sister to wife; and she bare him Aaron and Moses: and the years of the life of Amram were an hundred and thirty and seven years."}
  },
  {
    "question": "What did the widow of Zarephath have left when Elijah asked for food?",
    "choices": ["A handful of meal and a little oil", "Two loaves of bread", "Nothing", "A cake and wine"],
    "correctIndex": 0,
    "reference": {"book": "1 Kings", "chapter": 17, "verse": "12"},
    "explanation": "The widow had only a handful of flour and a little oil, planning to make one last meal before dying.",
    "verses": {"kjv": "And she said, As the LORD thy God liveth, I have not a cake, but an handful of meal in a barrel, and a little oil in a cruse: and, behold, I am gathering two sticks, that I may go in and dress it for me and my son, that we may eat it, and die."}
  },
  {
    "question": "Which woman was described as 'a woman of a sorrowful spirit' when praying for a son?",
    "choices": ["Hannah", "Rachel", "Sarah", "Elizabeth"],
    "correctIndex": 0,
    "reference": {"book": "1 Samuel", "chapter": 1, "verse": "15"},
    "explanation": "Hannah was praying silently in bitterness of soul when Eli the priest thought she was drunk.",
    "verses": {"kjv": "And Hannah answered and said, No, my lord, I am a woman of a sorrowful spirit: I have drunk neither wine nor strong drink, but have poured out my soul before the LORD."}
  },
  {
    "question": "What was the name of Ruth's son?",
    "choices": ["Obed", "Jesse", "Boaz", "Salmon"],
    "correctIndex": 0,
    "reference": {"book": "Ruth", "chapter": 4, "verse": "17"},
    "explanation": "Ruth bore Obed, who became the father of Jesse, who was the father of David.",
    "verses": {"kjv": "And the women her neighbours gave it a name, saying, There is a son born to Naomi; and they called his name Obed: he is the father of Jesse, the father of David."}
  },
  {
    "question": "Which prophetess spoke about Jesus when He was presented at the temple as an infant?",
    "choices": ["Anna", "Deborah", "Huldah", "Miriam"],
    "correctIndex": 0,
    "reference": {"book": "Luke", "chapter": 2, "verse": "36-38"},
    "explanation": "Anna, an 84-year-old prophetess, gave thanks and spoke of Jesus to all who awaited redemption.",
    "verses": {"kjv": "And there was one Anna, a prophetess, the daughter of Phanuel, of the tribe of Aser: she was of a great age, and had lived with an husband seven years from her virginity; And she was a widow of about fourscore and four years, which departed not from the temple, but served God with fastings and prayers night and day. And she coming in that instant gave thanks likewise unto the Lord, and spake of him to all them that looked for redemption in Jerusalem."}
  },
  {
    "question": "Who was the mother of John the Baptist?",
    "choices": ["Elisabeth", "Mary", "Anna", "Salome"],
    "correctIndex": 0,
    "reference": {"book": "Luke", "chapter": 1, "verse": "57"},
    "explanation": "Elisabeth, wife of Zacharias, gave birth to John in her old age after being barren.",
    "verses": {"kjv": "Now Elisabeth's full time came that she should be delivered; and she brought forth a son."}
  },
  {
    "question": "What relation was Elisabeth to Mary the mother of Jesus?",
    "choices": ["Cousin (or kinswoman)", "Sister", "Aunt", "Mother-in-law"],
    "correctIndex": 0,
    "reference": {"book": "Luke", "chapter": 1, "verse": "36"},
    "explanation": "The angel told Mary that her cousin Elisabeth had also conceived a son in her old age.",
    "verses": {"kjv": "And, behold, thy cousin Elisabeth, she hath also conceived a son in her old age: and this is the sixth month with her, who was called barren."}
  },
  {
    "question": "Which woman touched Jesus' garment and was healed?",
    "choices": ["The woman with the issue of blood", "Mary Magdalene", "Martha", "Joanna"],
    "correctIndex": 0,
    "reference": {"book": "Matthew", "chapter": 9, "verse": "20-22"},
    "explanation": "A woman who had hemorrhaged for twelve years touched the hem of Jesus' garment and was immediately healed.",
    "verses": {"kjv": "And, behold, a woman, which was diseased with an issue of blood twelve years, came behind him, and touched the hem of his garment: For she said within herself, If I may but touch his garment, I shall be whole. But Jesus turned him about, and when he saw her, he said, Daughter, be of good comfort; thy faith hath made thee whole. And the woman was made whole from that hour."}
  },
  {
    "question": "How did Dinah, Jacob's daughter, come to be defiled?",
    "choices": ["Shechem the Hivite took and violated her", "She was captured in war", "She fell into sin willingly", "She was deceived by false gods"],
    "correctIndex": 0,
    "reference": {"book": "Genesis", "chapter": 34, "verse": "2"},
    "explanation": "Shechem, son of Hamor the Hivite, saw Dinah and took her and defiled her.",
    "verses": {"kjv": "And when Shechem the son of Hamor the Hivite, prince of the country, saw her, he took her, and lay with her, and defiled her."}
  },
  {
    "question": "Which woman did Priscilla and her husband Aquila instruct in the way of God more perfectly?",
    "choices": ["They instructed Apollos, a man", "Lydia", "Phoebe", "Mary"],
    "correctIndex": 0,
    "reference": {"book": "Acts", "chapter": 18, "verse": "26"},
    "explanation": "Priscilla and Aquila heard Apollos speak and took him aside to explain the way of God more accurately.",
    "verses": {"kjv": "And he began to speak boldly in the synagogue: whom when Aquila and Priscilla had heard, they took him unto them, and expounded unto him the way of God more perfectly."}
  },
  {
    "question": "What was the name of Naaman's wife's Israelite maid who told of Elisha?",
    "choices": ["The Bible doesn't give her name", "Miriam", "Deborah", "Ruth"],
    "correctIndex": 0,
    "reference": {"book": "2 Kings", "chapter": 5, "verse": "2-3"},
    "explanation": "The little maid from Israel is never named, but she testified that the prophet in Samaria could cure Naaman.",
    "verses": {"kjv": "And the Syrians had gone out by companies, and had brought away captive out of the land of Israel a little maid; and she waited on Naaman's wife. And she said unto her mistress, Would God my lord were with the prophet that is in Samaria! for he would recover him of his leprosy."}
  },
  {
    "question": "Which woman was turned into a pillar of salt?",
    "choices": ["Lot's wife", "Lot's daughter", "Sarah", "Hagar"],
    "correctIndex": 0,
    "reference": {"book": "Genesis", "chapter": 19, "verse": "26"},
    "explanation": "Lot's wife looked back at the destruction of Sodom and Gomorrah and became a pillar of salt.",
    "verses": {"kjv": "But his wife looked back from behind him, and she became a pillar of salt."}
  },
  {
    "question": "What was the name of Moses' wife?",
    "choices": ["Zipporah", "Miriam", "Deborah", "Jochebed"],
    "correctIndex": 0,
    "reference": {"book": "Exodus", "chapter": 2, "verse": "21"},
    "explanation": "Moses married Zipporah, the daughter of Jethro (Reuel), the priest of Midian.",
    "verses": {"kjv": "And Moses was content to dwell with the man: and he gave Moses Zipporah his daughter."}
  },
  {
    "question": "Which woman was commended for showing hospitality to Elisha by preparing a room for him?",
    "choices": ["The Shunammite woman", "The widow of Zarephath", "Rahab", "Lydia"],
    "correctIndex": 0,
    "reference": {"book": "2 Kings", "chapter": 4, "verse": "9-10"},
    "explanation": "The wealthy woman of Shunem prepared a room on the wall for Elisha with a bed, table, stool, and candlestick.",
    "verses": {"kjv": "And she said unto her husband, Behold now, I perceive that this is an holy man of God, which passeth by us continually. Let us make a little chamber, I pray thee, on the wall; and let us set for him there a bed, and a table, and a stool, and a candlestick: and it shall be, when he cometh to us, that he shall turn in thither."}
  },
  {
    "question": "Who was the mother of James and John, the sons of Zebedee?",
    "choices": ["Salome", "Mary", "Martha", "Joanna"],
    "correctIndex": 0,
    "reference": {"book": "Matthew", "chapter": 27, "verse": "56"},
    "explanation": "Salome, identified as the mother of Zebedee's children, was present at the crucifixion.",
    "verses": {"kjv": "Among which was Mary Magdalene, and Mary the mother of James and Joses, and the mother of Zebedee's children."}
  },
  {
    "question": "Which woman had seven demons cast out of her by Jesus?",
    "choices": ["Mary Magdalene", "Mary of Bethany", "Joanna", "Susanna"],
    "correctIndex": 0,
    "reference": {"book": "Luke", "chapter": 8, "verse": "2"},
    "explanation": "Mary Magdalene had seven devils cast out of her and became a devoted follower of Jesus.",
    "verses": {"kjv": "And certain women, which had been healed of evil spirits and infirmities, Mary called Magdalene, out of whom went seven devils,"}
  },
  {
    "question": "What did the sinful woman anoint Jesus' feet with?",
    "choices": ["Ointment and her tears", "Oil", "Perfume only", "Water"],
    "correctIndex": 0,
    "reference": {"book": "Luke", "chapter": 7, "verse": "38"},
    "explanation": "The woman stood at Jesus' feet weeping, washed them with tears, and anointed them with ointment.",
    "verses": {"kjv": "And stood at his feet behind him weeping, and began to wash his feet with tears, and did wipe them with the hairs of her head, and kissed his feet, and anointed them with the ointment."}
  },
  {
    "question": "How many pieces of silver did the woman who lost one piece have originally?",
    "choices": ["Ten", "Seven", "Twelve", "Five"],
    "correctIndex": 0,
    "reference": {"book": "Luke", "chapter": 15, "verse": "8"},
    "explanation": "In Jesus' parable, the woman had ten pieces of silver and lost one, then swept diligently to find it.",
    "verses": {"kjv": "Either what woman having ten pieces of silver, if she lose one piece, doth not light a candle, and sweep the house, and seek diligently till she find it?"}
  },
  {
    "question": "Which woman was the first to see the risen Jesus?",
    "choices": ["Mary Magdalene", "Mary the mother of Jesus", "Joanna", "Salome"],
    "correctIndex": 0,
    "reference": {"book": "John", "chapter": 20, "verse": "14-16"},
    "explanation": "Mary Magdalene was the first person to see Jesus after His resurrection, initially thinking He was the gardener.",
    "verses": {"kjv": "And when she had thus said, she turned herself back, and saw Jesus standing, and knew not that it was Jesus. Jesus saith unto her, Woman, why weepest thou? whom seekest thou? She, supposing him to be the gardener, saith unto him, Sir, if thou have borne him hence, tell me where thou hast laid him, and I will take him away. Jesus saith unto her, Mary. She turned herself, and saith unto him, Rabboni; which is to say, Master."}
  },
  {
    "question": "Which woman was praised for choosing the better part by sitting at Jesus' feet?",
    "choices": ["Mary of Bethany", "Martha", "Mary Magdalene", "Joanna"],
    "correctIndex": 0,
    "reference": {"book": "Luke", "chapter": 10, "verse": "42"},
    "explanation": "While Martha was distracted with serving, Mary sat at Jesus' feet hearing His word, which Jesus said was the better choice.",
    "verses": {"kjv": "But one thing is needful: and Mary hath chosen that good part, which shall not be taken away from her."}
  }
]

# Add IDs and theme/difficulty
for i, q in enumerate(new_questions, start=12):
    q['id'] = f"WOM-H-{i:04d}"
    q['theme'] = "Women of Faith"
    q['difficulty'] = "hard"
    existing.append(q)

# Save
with open('app/public/questions/women-of-faith/hard.json', 'w', encoding='utf-8') as f:
    json.dump(existing, f, indent=2, ensure_ascii=False)

print(f"✅ Added {len(new_questions)} questions!")
print(f"New total: {len(existing)} questions")
print(f"IDs: WOM-H-0001 through WOM-H-{len(existing):04d}")

# Update index
with open('app/public/questions/index.json', 'r', encoding='utf-8') as f:
    index = json.load(f)

for entry in index:
    if entry.get('themePath') == 'women-of-faith' and entry.get('difficulty') == 'hard':
        entry['count'] = len(existing)

with open('app/public/questions/index.json', 'w', encoding='utf-8') as f:
    json.dump(index, f, indent=2, ensure_ascii=False)

print("✅ Index updated!")
