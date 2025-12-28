import json
import os

# Base path
base_path = "app/public/questions"

themes = [
    ("miracles", "Miracles"),
    ("prophets", "Prophets"),
    ("apostles", "Apostles"),
    ("kings-rulers", "Kings & Rulers"),
    ("women-of-faith", "Women of Faith"),
    ("battles-conquests", "Battles & Conquests"),
    ("parables-teachings", "Parables & Teachings"),
    ("creation-origins", "Creation & Origins"),
    ("prophecy-end-times", "Prophecy & End Times"),
    ("journeys-exile", "Journeys & Exile"),
    ("festivals-customs", "Festivals & Customs"),
    ("wisdom-psalms", "Wisdom & Psalms")
]

print("=" * 60)
print("QUESTION COUNT VERIFICATION")
print("=" * 60)

total = 0
all_balanced = True

for theme_path, theme_name in themes:
    easy_count = len(json.load(open(f"{base_path}/{theme_path}/easy.json", 'r', encoding='utf-8')))
    medium_count = len(json.load(open(f"{base_path}/{theme_path}/medium.json", 'r', encoding='utf-8')))
    hard_count = len(json.load(open(f"{base_path}/{theme_path}/hard.json", 'r', encoding='utf-8')))
    theme_total = easy_count + medium_count + hard_count
    
    status = "✅" if theme_total == 80 else "❌"
    print(f"{status} {theme_name:25} Easy: {easy_count:2} | Medium: {medium_count:2} | Hard: {hard_count:2} | Total: {theme_total}")
    
    total += theme_total
    if theme_total != 80:
        all_balanced = False

print("=" * 60)
print(f"GRAND TOTAL: {total} questions")
print("=" * 60)

if all_balanced:
    print("🎉 All themes perfectly balanced at 80 questions each!")
else:
    print("⚠️  Some themes need adjustment")
