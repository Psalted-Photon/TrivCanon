import json
import subprocess

# Get the git diff to see what was removed
result = subprocess.run(['git', 'diff', 'HEAD', 'app/public/questions.json'], 
                       capture_output=True, text=True, cwd=r'C:\Users\Marlowe\Bible Trivia')

# Parse removed Women of Faith questions
lines = result.stdout.split('\n')
removed_questions = []
current_question = {}
in_removed = False

for i, line in enumerate(lines):
    if line.startswith('-') and not line.startswith('---'):
        in_removed = True
        line = line[1:].strip()
        
        if '"theme": "Women of Faith"' in line:
            current_question = {'theme': 'Women of Faith'}
        elif '"id":' in line and current_question:
            current_question['id'] = line
        elif '"question":' in line and current_question:
            current_question['question'] = line.split('"question": "')[1].split('",')[0] if '"question": "' in line else ''
            if current_question.get('question'):
                removed_questions.append(current_question.get('question'))
                
print(f"Found {len(removed_questions)} Women of Faith questions that were removed")
print("\nFirst 10 removed Women of Faith questions:")
for i, q in enumerate(removed_questions[:10], 1):
    print(f"{i}. {q}")
