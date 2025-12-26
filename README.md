# TrivCanon - Master the Canon

A progressive web app for competitive Bible trivia. Test your biblical knowledge across 12 scriptural themes with 1200+ questions. Clean, modern interface with an authoritative edge—where Bible mastery meets competitive gaming.

**Brand Essence:** The definitive test of biblical knowledge.

## 12 Themes
1. **Miracles** - Healings, supernatural events, divine interventions
2. **Prophets** - Isaiah, Jeremiah, Elijah, prophetic messages
3. **Apostles** - The twelve disciples, Paul's journeys, early church
4. **Kings & Rulers** - David, Solomon, Saul, Pharaohs, Herod
5. **Women of Faith** - Ruth, Esther, Mary, Deborah, brave women
6. **Battles & Conquests** - Jericho, David vs Goliath, spiritual warfare
7. **Parables & Teachings** - Good Samaritan, Prodigal Son, Jesus' lessons
8. **Creation & Origins** - Genesis, Garden of Eden, Noah's ark
9. **Prophecy & End Times** - Revelation, Daniel's visions, Messianic prophecy
10. **Journeys & Exile** - Exodus, Babylonian captivity, missionary journeys
11. **Festivals & Customs** - Passover, Sabbath, Pentecost, Jewish traditions
12. **Wisdom & Psalms** - Proverbs, Ecclesiastes, David's songs

## Translation

- **Verse Text:** World English Bible (WEB) - public domain, unrestricted use
- **References:** KJV format for compatibility with theographic metadata

## Brand Identity

**TrivCanon** — Confident. Scholarly. Minimal. Competitive.

**Color Palette:**
- Deep Navy (#1a2332) — authority, Scripture
- Gold (#d4af37) — canon, mastery, value
- Ivory (#faf9f6) — biblical text, parchment feel
- Slate Gray (#475569) — modern, clean UI

**Typography:**
- Headings/Titles: Milonga (cursive)
- Body/UI: System sans-serif

**Future Features:**
- Game modes: Streak runs, timed challenges, fixed question sets (10/50/100)
- Multiplayer: 1-12 player support for competitive and cooperative play
- Stats tracking: Canon Rank (global score), performance analytics

## Quick Start

### 1. Install Dependencies
```powershell
pip install -r requirements.txt
```

### 2. Download Data Sources
```powershell
# From the project root
python download_data.py
```

### 3. Set API Key
```powershell
$env:ANTHROPIC_API_KEY="your-api-key-here"
```

### 4. Generate Questions
```powershell
python generator/generate_questions.py
```

This will generate 1200 questions (100 per theme) and save to `output/questions.json`.

### 5. Run the Web App
```powershell
cd app
npm install
npm run dev
```

Visit `http://localhost:5173` to play TrivCanon.

## Project Structure

```
Bible Trivia/
├── data/                      # Bible databases (downloaded)
│   ├── bible.db              # scrollmapper SQLite (WEB + KJV)
│   ├── people.json           # theographic people data
│   ├── places.json           # theographic places data
│   └── events.json           # theographic events data
├── generator/                 # Question generation scripts
│   ├── config.py             # Configuration
│   ├── bible_data.py         # Data access layer
│   ├── question_templates.py # Template generators
│   ├── claude_generator.py   # Claude API integration
│   └── generate_questions.py # Main script
├── output/
│   └── questions.json        # Generated questions
└── app/                       # React PWA (coming next)
```

## Question Schema

```json
{
  "id": 1,
  "theme": "Miracles",
  "question": "Who turned water into wine at a wedding?",
  "choices": ["Jesus", "Moses", "Elijah", "Peter"],
  "correctIndex": 0,
  "difficulty": "easy",
  "reference": {
    "book": "John",
    "chapter": 2,
    "verse": "1-11"
  },
  "explanation": "Jesus performed his first miracle at a wedding in Cana."
}
```

## Tech Stack

- **Question Generator:** Python 3.8+ with SQLite, Claude 4.5 Sonnet API
- **Bible Data:** scrollmapper (WEB translation) + theographic (metadata)
- **Web App:** React 18 + Vite + PWA
- **Offline Storage:** IndexedDB with Workbox
- **Deployment:** Netlify
