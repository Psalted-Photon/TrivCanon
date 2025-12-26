"""Quick test to generate 5 sample questions to verify the pipeline."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / 'generator'))

import config
from bible_data import BibleData
from question_templates import QuestionTemplates
from claude_generator import ClaudeGenerator

def main():
    print("="*60)
    print("Bible Trivia Pipeline Test - Generating 5 Sample Questions")
    print("="*60 + "\n")
    
    # Check API key
    if not config.ANTHROPIC_API_KEY:
        print("❌ ERROR: ANTHROPIC_API_KEY not set!")
        print("\nSet with: $env:ANTHROPIC_API_KEY='your-key-here'")
        return
    
    print("✓ API key found")
    print("\nInitializing components...")
    
    bible = BibleData(config.DATA_DIR)
    templates = QuestionTemplates(bible)
    claude = ClaudeGenerator(config.ANTHROPIC_API_KEY, config.CLAUDE_MODEL)
    
    print("✓ Components initialized\n")
    
    # Test 5 different themes
    test_themes = ['Miracles', 'Prophets', 'Apostles', 'Kings & Rulers', 'Wisdom & Psalms']
    
    for i, theme in enumerate(test_themes, 1):
        print(f"\n[{i}/5] Generating question for theme: {theme}")
        print("-" * 60)
        
        try:
            # Generate template
            template_data = templates.generate_for_theme(theme)
            verse = template_data.get('verse', {})
            print(f"Verse: {verse.get('book')} {verse.get('chapter')}:{verse.get('verse')}")
            print(f"Text: {verse.get('text', '')[:80]}...")
            
            # Generate question
            print("\nCalling Claude API...")
            question = claude.generate_question(template_data, 'medium')
            
            print(f"\n✓ Question generated successfully!")
            print(f"\nQ: {question['question']}")
            print(f"Choices:")
            for j, choice in enumerate(question['choices']):
                marker = "✓" if j == question['correctIndex'] else " "
                print(f"  [{marker}] {choice}")
            print(f"\nExplanation: {question.get('explanation', 'N/A')}")
            
        except Exception as e:
            print(f"\n❌ Error: {e}")
            import traceback
            traceback.print_exc()
            return
    
    bible.close()
    
    print("\n" + "="*60)
    print("✓ All test questions generated successfully!")
    print("✓ Pipeline is working. Ready to generate full question bank.")
    print("="*60)

if __name__ == "__main__":
    main()
