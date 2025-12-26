"""Configuration for Bible trivia question generator."""

import os

# Bible translation settings
# KJV for metadata references (theographic compatibility)
# WEB for displayed verse text (public domain, unrestricted)
KJV_TRANSLATION = 'kjv'
WEB_TRANSLATION = 'web'
DISPLAY_TRANSLATION = WEB_TRANSLATION  # Translation shown to users

# Anthropic API configuration
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY', '')
CLAUDE_MODEL = 'claude-sonnet-4.5'

# Question generation targets
QUESTIONS_PER_THEME = 100
THEMES = [
    "Miracles",
    "Prophets", 
    "Apostles",
    "Kings & Rulers",
    "Women of Faith",
    "Battles & Conquests",
    "Parables & Teachings",
    "Creation & Origins",
    "Prophecy & End Times",
    "Journeys & Exile",
    "Festivals & Customs",
    "Wisdom & Psalms"
]

# Difficulty distribution (percentages)
DIFFICULTY_DISTRIBUTION = {
    'easy': 0.40,    # 40% easy
    'medium': 0.40,  # 40% medium
    'hard': 0.20     # 20% hard
}

# Paths
DATA_DIR = 'data'
OUTPUT_DIR = 'output'
OUTPUT_FILE = 'questions.json'
