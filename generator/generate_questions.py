"""Main script to generate Bible trivia questions."""

import json
import random
import sys
from pathlib import Path
from tqdm import tqdm

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

import config
from bible_data import BibleData
from question_templates import QuestionTemplates
from claude_generator import ClaudeGenerator


def generate_difficulty() -> str:
    """Generate difficulty based on distribution."""
    rand = random.random()
    cumulative = 0
    
    for difficulty, prob in config.DIFFICULTY_DISTRIBUTION.items():
        cumulative += prob
        if rand <= cumulative:
            return difficulty
    
    return 'medium'  # fallback


def shuffle_choices(question_data: Dict, correct_index: int) -> Dict:
    """Shuffle choices and update correctIndex accordingly."""
    choices = question_data['choices']
    correct_answer = choices[correct_index]
    
    # Shuffle
    random.shuffle(choices)
    
    # Find new index of correct answer
    new_correct_index = choices.index(correct_answer)
    
    return {
        **question_data,
        'choices': choices,
        'correctIndex': new_correct_index
    }


def main():
    print("="*60)
    print("Bible Trivia Question Generator")
    print("="*60)
    print(f"Translation: KJV (Public Domain)")
    print(f"Target: {config.QUESTIONS_PER_THEME} questions per theme")
    print(f"Total themes: {len(config.THEMES)}")
    print(f"Total questions: {len(config.THEMES) * config.QUESTIONS_PER_THEME}")
    print("="*60 + "\n")
    
    # Check API key
    if not config.ANTHROPIC_API_KEY:
        print("ERROR: ANTHROPIC_API_KEY environment variable not set!")
        print("\nSet it with:")
        print('  PowerShell: $env:ANTHROPIC_API_KEY="your-key-here"')
        print('  CMD: set ANTHROPIC_API_KEY=your-key-here')
        sys.exit(1)
    
    # Initialize components
    print("Loading Bible data...")
    bible_data = BibleData(config.DATA_DIR)
    print(f"✓ Loaded {len(bible_data.people)} people, {len(bible_data.places)} places, {len(bible_data.events)} events")
    
    templates = QuestionTemplates(bible_data)
    claude = ClaudeGenerator(config.ANTHROPIC_API_KEY, config.CLAUDE_MODEL)
    
    # Output structure
    all_questions = []
    question_id = 1
    
    # Generate questions for each theme
    for theme in config.THEMES:
        print(f"\n{'='*60}")
        print(f"Theme: {theme}")
        print(f"Generating {config.QUESTIONS_PER_THEME} questions...")
        print('='*60)
        
        theme_questions = []
        
        with tqdm(total=config.QUESTIONS_PER_THEME, desc=theme, unit="q") as pbar:
            attempts = 0
            max_attempts = config.QUESTIONS_PER_THEME * 3  # Allow some failures
            
            while len(theme_questions) < config.QUESTIONS_PER_THEME and attempts < max_attempts:
                attempts += 1
                
                try:
                    # Generate template data
                    template_data = templates.generate_for_theme(theme)
                    difficulty = generate_difficulty()
                    
                    # Generate question via Claude
                    question_data = claude.generate_question(template_data, difficulty)
                    
                    # Shuffle choices so correct answer isn't always first
                    question_data = shuffle_choices(question_data, question_data.get('correctIndex', 0))
                    
                    # Build final question structure
                    question = {
                        'id': question_id,
                        'theme': theme,
                        'question': question_data['question'],
                        'choices': question_data['choices'],
                        'correctIndex': question_data['correctIndex'],
                        'difficulty': difficulty,
                        'reference': {
                            'book': template_data.get('verse', {}).get('book', 'Unknown'),
                            'chapter': template_data.get('verse', {}).get('chapter', 0),
                            'verse': template_data.get('verse', {}).get('verse', 0)
                        },
                        'explanation': question_data.get('explanation', '')
                    }
                    
                    theme_questions.append(question)
                    all_questions.append(question)
                    question_id += 1
                    pbar.update(1)
                    
                except KeyboardInterrupt:
                    print("\n\nInterrupted by user. Saving progress...")
                    break
                except Exception as e:
                    pbar.write(f"Error: {str(e)[:100]}")
                    continue
            
            if len(theme_questions) < config.QUESTIONS_PER_THEME:
                print(f"\n⚠ Warning: Only generated {len(theme_questions)}/{config.QUESTIONS_PER_THEME} questions for {theme}")
        
        print(f"✓ Completed {theme}: {len(theme_questions)} questions")
    
    # Save to file
    output_path = Path(config.OUTPUT_DIR) / config.OUTPUT_FILE
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)
    
    print("\n" + "="*60)
    print(f"✓ Generation complete!")
    print(f"✓ Total questions generated: {len(all_questions)}")
    print(f"✓ Output file: {output_path.absolute()}")
    print("="*60)
    
    # Stats
    print("\n📊 Statistics:")
    print(f"\nQuestions by theme:")
    for theme in config.THEMES:
        count = sum(1 for q in all_questions if q['theme'] == theme)
        print(f"  {theme}: {count}")
    
    print(f"\nDifficulty distribution:")
    for diff in ['easy', 'medium', 'hard']:
        count = sum(1 for q in all_questions if q['difficulty'] == diff)
        percentage = (count / len(all_questions) * 100) if all_questions else 0
        print(f"  {diff.capitalize()}: {count} ({percentage:.1f}%)")
    
    bible_data.close()
    print("\n✓ Done!")


if __name__ == "__main__":
    main()
