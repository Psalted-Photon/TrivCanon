"""Test script to verify Bible data loads correctly."""

import sys
from pathlib import Path

# Add generator to path
sys.path.insert(0, str(Path(__file__).parent / 'generator'))

from bible_data import BibleData
import config

def main():
    print("="*60)
    print("Bible Data Verification Test")
    print("="*60 + "\n")
    
    try:
        # Load data
        print("Loading Bible data...")
        bible = BibleData(config.DATA_DIR)
        
        # Test verse retrieval
        print("\n✓ Database loaded successfully!")
        print(f"  Verse table: {bible.verse_table}")
        print(f"  Books table: {bible.books_table}")
        
        # Test theographic data
        print(f"\n✓ Theographic data loaded:")
        print(f"  People: {len(bible.people):,}")
        print(f"  Places: {len(bible.places):,}")
        print(f"  Events: {len(bible.events):,}")
        
        # Get random verse
        print("\n📖 Random verse test:")
        verse = bible.get_random_verse()
        print(f"  {verse['book']} {verse['chapter']}:{verse['verse']}")
        print(f"  \"{verse['text']}\"")
        
        # Get random person
        print("\n👤 Random person test:")
        person = bible.get_random_person()
        if person:
            print(f"  Name: {person.get('name', 'Unknown')}")
            print(f"  Gender: {person.get('gender', 'Unknown')}")
            print(f"  Verses: {person.get('verseCount', 0)}")
        
        bible.close()
        
        print("\n" + "="*60)
        print("✓ All tests passed! Ready to generate questions.")
        print("="*60)
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
