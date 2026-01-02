"""
Generate questions to reach target of 50 easy, 50 medium, 50 hard per theme.
Maximum 84 questions generated per run.

Simple workflow:
1. Run this script and select a theme
2. Script shows current counts and generates a prompt
3. Copy the prompt and paste it to Claude (via GitHub Copilot agent mode)
4. Claude generates the questions directly into the JSON files
"""

import json
from pathlib import Path

# Theme configuration
THEMES = {
    "1": {"name": "Apostles", "folder": "apostles", "prefix": "APO"},
    "2": {"name": "Battles & Conquests", "folder": "battles-conquests", "prefix": "BAT"},
    "3": {"name": "Creation & Origins", "folder": "creation-origins", "prefix": "CRE"},
    "4": {"name": "Festivals & Customs", "folder": "festivals-customs", "prefix": "FES"},
    "5": {"name": "Journeys & Exile", "folder": "journeys-exile", "prefix": "JRN"},
    "6": {"name": "Kings & Rulers", "folder": "kings-rulers", "prefix": "KNG"},
    "7": {"name": "Miracles", "folder": "miracles", "prefix": "MIR"},
    "8": {"name": "Parables & Teachings", "folder": "parables-teachings", "prefix": "PAR"},
    "9": {"name": "Prophecy & End Times", "folder": "prophecy-end-times", "prefix": "END"},
    "10": {"name": "Prophets", "folder": "prophets", "prefix": "PRO"},
    "11": {"name": "Wisdom & Psalms", "folder": "wisdom-psalms", "prefix": "WIS"},
    "12": {"name": "Women of Faith", "folder": "women-of-faith", "prefix": "WOM"}
}

DIFFICULTIES = ["easy", "medium", "hard"]
DIFFICULTY_ABBREV = {"easy": "E", "medium": "M", "hard": "H"}
TARGET_PER_DIFFICULTY = 50
MAX_GENERATION = 84


def count_theme_questions(theme_folder):
    """Count existing questions for a theme across all difficulty levels."""
    base_path = Path(__file__).parent / "app" / "public" / "questions" / theme_folder
    counts = {"easy": 0, "medium": 0, "hard": 0}
    next_ids = {"easy": None, "medium": None, "hard": None}
    
    for difficulty in DIFFICULTIES:
        file_path = base_path / f"{difficulty}.json"
        if file_path.exists():
            with open(file_path, 'r', encoding='utf-8') as f:
                questions = json.load(f)
                counts[difficulty] = len(questions)
    
    return counts


def get_next_ids(theme_folder, theme_prefix):
    """Get the next ID for each difficulty level."""
    base_path = Path(__file__).parent / "app" / "public" / "questions" / theme_folder
    next_ids = {}
    
    for difficulty in DIFFICULTIES:
        file_path = base_path / f"{difficulty}.json"
        diff_abbrev = DIFFICULTY_ABBREV[difficulty]
        prefix = f"{theme_prefix}-{diff_abbrev}-"
        
        max_num = 0
        if file_path.exists():
            with open(file_path, 'r', encoding='utf-8') as f:
                questions = json.load(f)
                for q in questions:
                    if q["id"].startswith(prefix):
                        num_str = q["id"].split("-")[-1]
                        try:
                            num = int(num_str)
                            max_num = max(max_num, num)
                        except ValueError:
                            continue
        
        next_ids[difficulty] = f"{prefix}{(max_num + 1):04d}"
    
    return next_ids


def calculate_needed(counts):
    """Calculate how many questions needed per difficulty, capped at MAX_GENERATION."""
    needed = {}
    for difficulty in DIFFICULTIES:
        current = counts[difficulty]
        if current < TARGET_PER_DIFFICULTY:
            needed[difficulty] = TARGET_PER_DIFFICULTY - current
        else:
            needed[difficulty] = 0
    
    # Apply 84 cap across all difficulties
    total_needed = sum(needed.values())
    if total_needed > MAX_GENERATION:
        # Proportionally reduce each difficulty
        scale = MAX_GENERATION / total_needed
        for difficulty in DIFFICULTIES:
            if needed[difficulty] > 0:
                needed[difficulty] = int(needed[difficulty] * scale)
    
    return needed


def display_menu():
    """Display theme selection menu."""
    print("\n" + "="*60)
    print(" "*15 + "BIBLE TRIVIA QUESTION GENERATOR")
    print("="*60)
    print("\nSelect a theme to generate questions for:\n")
    
    for num in sorted(THEMES.keys(), key=int):
        theme_info = THEMES[num]
        print(f"  {num:2}. {theme_info['name']}")
    
    print("\n   0. Exit")
    print("\n" + "="*60)


def display_generation_plan(theme_name, counts, needed, next_ids):
    """Display current status and generation prompt for Claude."""
    print(f"\n{'='*60}")
    print(f" Theme: {theme_name}")
    print(f"{'='*60}\n")
    
    print("Current Status:")
    total_current = sum(counts.values())
    print(f"  Easy:   {counts['easy']}/50")
    print(f"  Medium: {counts['medium']}/50")
    print(f"  Hard:   {counts['hard']}/50")
    print(f"  Total:  {total_current}/150\n")
    
    total_needed = sum(needed.values())
    if total_needed == 0:
        print("✓ This theme is complete! All difficulties have 50 questions.")
        return None
    
    print("Questions to Generate:")
    print(f"  Easy:   {needed['easy']} questions (starting at {next_ids['easy']})")
    print(f"  Medium: {needed['medium']} questions (starting at {next_ids['medium']})")
    print(f"  Hard:   {needed['hard']} questions (starting at {next_ids['hard']})")
    print(f"  Total:  {total_needed} questions\n")
    
    if total_needed > MAX_GENERATION:
        print(f"  Note: Capped at {MAX_GENERATION} questions per run\n")
    
    # Build the prompt for Claude
    prompt = f"""Generate {total_needed} Bible trivia questions for the "{theme_name}" theme.

DISTRIBUTION:
"""
    
    if needed['easy'] > 0:
        start_num = int(next_ids['easy'].split('-')[-1])
        end_num = TARGET_PER_DIFFICULTY
        prompt += f"- {needed['easy']} EASY questions (IDs: {next_ids['easy'].rsplit('-', 1)[0]}-{start_num:04d} to {next_ids['easy'].rsplit('-', 1)[0]}-{end_num:04d})\n"
    
    if needed['medium'] > 0:
        start_num = int(next_ids['medium'].split('-')[-1])
        end_num = TARGET_PER_DIFFICULTY
        prompt += f"- {needed['medium']} MEDIUM questions (IDs: {next_ids['medium'].rsplit('-', 1)[0]}-{start_num:04d} to {next_ids['medium'].rsplit('-', 1)[0]}-{end_num:04d})\n"
    
    if needed['hard'] > 0:
        start_num = int(next_ids['hard'].split('-')[-1])
        end_num = TARGET_PER_DIFFICULTY
        prompt += f"- {needed['hard']} HARD questions (IDs: {next_ids['hard'].rsplit('-', 1)[0]}-{start_num:04d} to {next_ids['hard'].rsplit('-', 1)[0]}-{end_num:04d})\n"
    
    prompt += f"""
REQUIREMENTS:
- Use KJV Bible only
- Each question has exactly 4 multiple choice answers
- correctIndex is 0-3 indicating which choice is correct
- Include book/chapter/verse reference
- Include full verse text in KJV in the "verses" field
- Include explanation of the answer

IMPORTANT: Add questions directly to these files:
"""
    
    base_path = "c:\\Users\\Marlowe\\Bible Trivia\\app\\public\\questions"
    for difficulty in DIFFICULTIES:
        if needed[difficulty] > 0:
            folder = THEMES[[k for k, v in THEMES.items() if v['name'] == theme_name][0]]['folder']
            prompt += f"- {base_path}\\{folder}\\{difficulty}.json ({needed[difficulty]} {difficulty} questions)\n"
    
    prompt += """
Each question must follow this exact structure:
{
  "id": "<use the sequential ID from the range above>",
  "theme": "<theme name>",
  "question": "<question text>",
  "choices": ["<correct answer>", "<wrong1>", "<wrong2>", "<wrong3>"],
  "correctIndex": 0,
  "difficulty": "<easy|medium|hard>",
  "reference": {"book": "<BookName>", "chapter": <number>, "verse": "<number or range>"},
  "explanation": "<why this answer is correct>",
  "verses": {"kjv": "<full verse text from KJV>"}
}

Load each file, append the new questions to the existing array, and save. Use proper JSON formatting with 2-space indentation."""
    
    return prompt


def main():
    """Main workflow loop."""
    while True:
        display_menu()
        
        choice = input("\nEnter theme number (or 0 to exit): ").strip()
        
        if choice == "0":
            print("\nExiting. Happy trivia building!")
            break
        
        if choice not in THEMES:
            print("\n❌ Invalid selection. Please choose 1-12 or 0 to exit.")
            continue
        
        theme_info = THEMES[choice]
        theme_name = theme_info["name"]
        theme_folder = theme_info["folder"]
        theme_prefix = theme_info["prefix"]
        
        # Count and calculate
        counts = count_theme_questions(theme_folder)
        needed = calculate_needed(counts)
        next_ids = get_next_ids(theme_folder, theme_prefix)
        
        # Display plan and get prompt
        prompt = display_generation_plan(theme_name, counts, needed, next_ids)
        
        if prompt is None:
            input("\nPress Enter to continue...")
            continue
        
        # Show the prompt
        print("="*60)
        print(" "*18 + "COPY THIS PROMPT:")
        print("="*60)
        print()
        print(prompt)
        print()
        print("="*60)
        print("\nCopy the prompt above and paste it to Claude in agent mode.")
        print("Claude will directly add the questions to the JSON files.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
