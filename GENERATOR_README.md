# Question Generator - Usage Guide

## Overview

`generate_to_target.py` automatically generates Bible trivia questions to reach the target of **50 easy, 50 medium, 50 hard** questions per theme (150 total per theme).

## Features

- ✅ **Interactive theme selection** - Choose which theme to work on
- ✅ **Automatic progress tracking** - Detects existing questions and calculates what's needed
- ✅ **Smart generation cap** - Maximum 84 questions per run to manage API costs
- ✅ **Auto-resume** - Run multiple times on same theme to complete it
- ✅ **Sequential filling** - Completes easy → medium → hard in order
- ✅ **Duplicate prevention** - Checks for duplicates during and after generation
- ✅ **Claude AI integration** - Uses Anthropic Claude Sonnet 4.5 for high-quality questions

## Prerequisites

### 1. API Key

Set your Anthropic API key as an environment variable:

**PowerShell:**
```powershell
$env:ANTHROPIC_API_KEY="your-key-here"
```

**CMD:**
```cmd
set ANTHROPIC_API_KEY=your-key-here
```

**Permanent (add to your PowerShell profile):**
```powershell
[System.Environment]::SetEnvironmentVariable('ANTHROPIC_API_KEY', 'your-key-here', 'User')
```

### 2. Required Files

Make sure these directories exist with all files:
- `generator/` - Contains Claude generator and templates
- `data/` - Contains Bible data (people.json, events.json, places.json, bible.db)
- `app/public/questions/` - Question files organized by theme

## Usage

### Basic Usage

1. Run the script:
```powershell
python generate_to_target.py
```

2. Select a theme from the menu (1-12)

3. Review the generation plan showing:
   - Current question counts
   - How many needed per difficulty
   - Total to be generated this run

4. Confirm to proceed (y/n)

5. Watch as questions are generated and saved

6. Review final status

### Example Session

```
============================================================
Bible Trivia Question Generator - Reach 50/50/50 Target
============================================================

Available Themes:

   1. Apostles
   2. Battles & Conquests
   3. Creation & Origins
   ...

Select theme number (1-12, or 'q' to quit): 1

============================================================
Theme: Apostles
============================================================

Current Status:
  Easy:   31 / 50 (need 19)
  Medium: 29 / 50 (need 21)
  Hard:   19 / 50 (need 31)

Total needed: 71
Will generate: 71 questions this run (max 84)
============================================================

Proceed with generation? (y/n): y

[Generation happens...]

============================================================
FINAL STATUS
============================================================

Apostles:
  Easy:   50 / 50
  Medium: 50 / 50
  Hard:   50 / 50

✓ Theme complete! 150/150 questions reached.
```

## Generation Cap

The script generates a **maximum of 84 questions per run** to:
- Manage API costs
- Allow you to stop/resume as needed
- Give flexibility for interruptions

If a theme needs more than 84 questions, simply run the script again and select the same theme. It will automatically pick up where it left off.

### Example Multi-Run Scenario

**First run:**
- Apostles needs 71 total
- Generates all 71 (under 84 cap)
- Theme complete!

**Another theme needing 100 questions:**
- First run: Generates 84 (cap reached)
- Second run: Generates remaining 16
- Theme complete!

## Question Generation Process

For each question generated:

1. **Template Selection** - Chooses appropriate template for the theme
2. **Claude API Call** - Generates question using AI
3. **Duplicate Check** - Verifies question isn't already in file
4. **Choice Shuffling** - Randomizes answer order
5. **ID Assignment** - Assigns sequential ID (e.g., APO-E-0032)
6. **Save to File** - Appends to appropriate JSON file
7. **Cleanup** - Runs duplicate removal after all generation

## Themes & Abbreviations

| # | Theme | Folder | ID Prefix |
|---|-------|--------|-----------|
| 1 | Apostles | apostles | APO |
| 2 | Battles & Conquests | battles-conquests | BAT |
| 3 | Creation & Origins | creation-origins | CRE |
| 4 | Festivals & Customs | festivals-customs | FES |
| 5 | Journeys & Exile | journeys-exile | JRN |
| 6 | Kings & Rulers | kings-rulers | KNG |
| 7 | Miracles | miracles | MIR |
| 8 | Parables & Teachings | parables-teachings | PAR |
| 9 | Prophecy & End Times | prophecy-end-times | END |
| 10 | Prophets | prophets | PRO |
| 11 | Wisdom & Psalms | wisdom-psalms | WIS |
| 12 | Women of Faith | women-of-faith | WOM |

## Question ID Format

Questions are assigned IDs in the format: `{THEME}-{DIFFICULTY}-{NUMBER}`

Examples:
- `APO-E-0001` - Apostles, Easy, Question 1
- `PAR-M-0042` - Parables & Teachings, Medium, Question 42
- `END-H-0015` - Prophecy & End Times, Hard, Question 15

## Troubleshooting

### "ANTHROPIC_API_KEY not set"
Set the environment variable as shown in Prerequisites section.

### "Generator modules not available"
Ensure the `generator/` directory exists with all required Python files:
- `claude_generator.py`
- `question_templates.py`
- `bible_data.py`
- `config.py`

### "Error initializing generator"
Check that the `data/` directory contains:
- `bible.db` (SQLite database)
- `people.json`
- `events.json`
- `places.json`

### Questions seem low quality
The generator uses Claude Sonnet 4.5 with carefully crafted prompts. If quality is an issue:
- Check your API key is valid
- Review the prompts in `generator/claude_generator.py`
- Manually review and delete poor questions, then run again

### Script interrupted
No problem! The script saves progress after each difficulty level. Just run it again on the same theme to continue.

## Tips

1. **Start with smaller themes** - Test on themes needing fewer questions first
2. **Review periodically** - Check generated questions for quality
3. **Use the duplicate remover** - Run `remove_duplicates.py` if you suspect issues
4. **Monitor API costs** - 84 questions per run helps control costs
5. **Multiple sessions** - Feel free to generate questions over multiple days

## Files Modified

The script modifies files in:
```
app/public/questions/{theme}/
  - easy.json
  - medium.json  
  - hard.json
```

Always commit your changes to git before running to have a backup!

## Goal

Complete all 12 themes with 150 questions each:
- **12 themes × 150 questions = 1,800 total questions**
- Current count: 986 questions
- Remaining needed: ~814 questions
- At 84 per run: ~10 runs to completion

Happy question generating! 🎉
