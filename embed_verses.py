import json
import os
import sys
import time
import argparse
from pathlib import Path
from urllib.parse import quote
import urllib.request

def fetch_verse(book, chapter, verse, retries=3):
    """Fetch verse text from bible-api.com with retry logic"""
    verse_str = str(verse)
    url = f"https://bible-api.com/{quote(book)}+{chapter}:{verse_str}?translation=kjv"
    
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(url, timeout=10) as response:
                data = json.loads(response.read().decode())
                return data.get('text', '').strip()
        except Exception as e:
            if attempt < retries - 1:
                wait_time = 2 ** attempt  # Exponential backoff: 1s, 2s, 4s
                print(f"  ⚠️  Retry {attempt + 1}/{retries} for {book} {chapter}:{verse_str} (waiting {wait_time}s)")
                time.sleep(wait_time)
            else:
                print(f"  ⚠️  Error fetching {book} {chapter}:{verse_str} - {e}")
                return None

def process_difficulty(difficulty):
    """Process all theme files for a specific difficulty level"""
    questions_dir = Path("app/public/questions")
    
    if not questions_dir.exists():
        print(f"❌ Error: Questions directory not found at {questions_dir}")
        return
    
    # Get all theme directories
    theme_dirs = [d for d in questions_dir.iterdir() if d.is_dir()]
    theme_dirs.sort()  # Process in alphabetical order
    
    print(f"\n{'='*60}")
    print(f"Processing {difficulty.upper()} difficulty")
    print(f"Found {len(theme_dirs)} theme directories")
    print(f"{'='*60}\n")
    
    total_questions = 0
    total_verses_added = 0
    total_files = 0
    
    for theme_dir in theme_dirs:
        file_path = theme_dir / f"{difficulty}.json"
        
        if not file_path.exists():
            print(f"⚠️  Skipping {theme_dir.name}/{difficulty}.json (file not found)")
            continue
        
        print(f"\n📂 Processing: {theme_dir.name}/{difficulty}.json")
        
        # Read the questions
        with open(file_path, 'r', encoding='utf-8') as f:
            questions = json.load(f)
        
        print(f"   Found {len(questions)} questions")
        
        questions_updated = 0
        
        for i, question in enumerate(questions, 1):
            # Check if verse already exists
            if 'verses' in question and question['verses'].get('kjv'):
                print(f"   [{i}/{len(questions)}] Already has verse: {question['id']}")
                continue
            
            # Get reference
            ref = question.get('reference', {})
            book = ref.get('book')
            chapter = ref.get('chapter')
            verse = ref.get('verse')
            
            if not all([book, chapter, verse]):
                print(f"   [{i}/{len(questions)}] ⚠️  Missing reference: {question.get('id', 'unknown')}")
                continue
            
            # Fetch verse text
            verse_text = fetch_verse(book, chapter, verse)
            
            if verse_text:
                question['verses'] = {'kjv': verse_text}
                questions_updated += 1
                print(f"   [{i}/{len(questions)}] ✓ Added verse: {book} {chapter}:{verse}")
            else:
                print(f"   [{i}/{len(questions)}] ✗ Failed to fetch: {book} {chapter}:{verse}")
            
            # Rate limiting - 250ms delay between requests to avoid hitting API limits
            time.sleep(0.25)
        
        # Write back to file
        if questions_updated > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(questions, f, indent=2, ensure_ascii=False)
            print(f"   💾 Saved {questions_updated} new verses to {file_path.name}")
        
        total_questions += len(questions)
        total_verses_added += questions_updated
        total_files += 1
    
    # Summary
    print(f"\n{'='*60}")
    print(f"✅ {difficulty.upper()} DIFFICULTY COMPLETE")
    print(f"{'='*60}")
    print(f"Files processed: {total_files}")
    print(f"Total questions: {total_questions}")
    print(f"Verses added: {total_verses_added}")
    print(f"{'='*60}\n")

def main():
    parser = argparse.ArgumentParser(description='Embed Bible verses in question JSON files')
    parser.add_argument('--difficulty', 
                       choices=['easy', 'medium', 'hard'],
                       required=True,
                       help='Difficulty level to process (easy, medium, or hard)')
    
    args = parser.parse_args()
    
    print(f"\n🔷 Bible Verse Embedder 🔷")
    print(f"Starting processing for {args.difficulty} questions...\n")
    
    process_difficulty(args.difficulty)
    
    print("✨ Processing complete!\n")

if __name__ == "__main__":
    main()
