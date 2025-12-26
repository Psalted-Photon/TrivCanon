"""Generate questions using Claude API."""

import anthropic
import json
import os
import time
from typing import Dict

class ClaudeGenerator:
    """Generate trivia questions using Claude 4.5 Sonnet."""
    
    def __init__(self, api_key: str = None, model: str = 'claude-sonnet-4.5'):
        self.api_key = api_key or os.getenv('ANTHROPIC_API_KEY')
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY must be set in environment or passed to constructor")
        
        self.model = model
        self.client = anthropic.Anthropic(api_key=self.api_key)
    
    def generate_question(self, template_data: Dict, difficulty: str = 'medium') -> Dict:
        """Generate a single trivia question from template data."""
        
        # Build prompt based on template type
        if template_data['template'] == 'verse_context':
            prompt = self._build_verse_prompt(template_data, difficulty)
        elif template_data['template'] == 'person_relationship':
            prompt = self._build_person_prompt(template_data, difficulty)
        else:
            prompt = self._build_generic_prompt(template_data, difficulty)
        
        # Call Claude API with retry logic
        max_retries = 3
        for attempt in range(max_retries):
            try:
                message = self.client.messages.create(
                    model=self.model,
                    max_tokens=1024,
                    temperature=0.7,
                    messages=[{
                        "role": "user",
                        "content": prompt
                    }]
                )
                
                # Parse response
                response_text = message.content[0].text
                question_data = self._parse_json_response(response_text)
                
                # Validate response
                self._validate_question(question_data)
                
                return question_data
                
            except anthropic.RateLimitError:
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)  # Exponential backoff
                    continue
                raise
            except (json.JSONDecodeError, KeyError, ValueError) as e:
                if attempt < max_retries - 1:
                    continue
                raise Exception(f"Failed to generate valid question after {max_retries} attempts: {e}")
    
    def _parse_json_response(self, response_text: str) -> Dict:
        """Parse JSON from Claude response, handling markdown code blocks."""
        try:
            # Try direct JSON parse first
            return json.loads(response_text)
        except json.JSONDecodeError:
            # Try extracting from markdown code block
            if '```json' in response_text:
                json_str = response_text.split('```json')[1].split('```')[0].strip()
                return json.loads(json_str)
            elif '```' in response_text:
                json_str = response_text.split('```')[1].split('```')[0].strip()
                return json.loads(json_str)
            else:
                raise
    
    def _validate_question(self, question_data: Dict):
        """Validate question structure."""
        required_fields = ['question', 'choices', 'correctIndex']
        
        for field in required_fields:
            if field not in question_data:
                raise ValueError(f"Missing required field: {field}")
        
        if not isinstance(question_data['choices'], list):
            raise ValueError("choices must be a list")
        
        if len(question_data['choices']) != 4:
            raise ValueError(f"Must have exactly 4 choices, got {len(question_data['choices'])}")
        
        if not isinstance(question_data['correctIndex'], int):
            raise ValueError("correctIndex must be an integer")
        
        if not (0 <= question_data['correctIndex'] <= 3):
            raise ValueError(f"correctIndex must be 0-3, got {question_data['correctIndex']}")
    
    def _build_verse_prompt(self, template_data: Dict, difficulty: str) -> str:
        """Build prompt for verse-based question."""
        verse = template_data['verse']
        theme = template_data['theme']
        hint = template_data.get('prompt_hint', '')
        
        return f"""You are a Bible trivia expert. Generate a multiple-choice question from this verse.

**Verse:** {verse['book']} {verse['chapter']}:{verse['verse']}
"{verse['text']}"

**Theme:** {theme}
**Focus:** {hint}
**Difficulty:** {difficulty}

**Requirements:**
- Question should test comprehension, NOT verse memorization or chapter/verse numbers
- Focus on WHO, WHAT, WHERE, WHY (characters, events, meanings, locations)
- Create 1 correct answer + 3 plausible but incorrect distractors
- Distractors should be theologically plausible and from similar biblical contexts
- Avoid trivial or "trick" questions
- Make it engaging and educational
- DO NOT ask about verse numbers, chapter numbers, or book names

**Output Format (JSON only, no markdown):**
{{
  "question": "Clear, engaging question text",
  "choices": ["Correct answer", "Distractor 1", "Distractor 2", "Distractor 3"],
  "correctIndex": 0,
  "explanation": "Brief explanation of the answer with reference"
}}

The correct answer should be at index 0. We will shuffle the choices later.

Generate the question now:"""
    
    def _build_person_prompt(self, template_data: Dict, difficulty: str) -> str:
        """Build prompt for person/relationship question."""
        person = template_data['person']
        theme = template_data['theme']
        
        person_name = person.get('name', 'Unknown')
        also_called = person.get('alsoCalled', '')
        gender = person.get('gender', 'Unknown')
        verse_count = person.get('verseCount', 0)
        
        context = f"**Person:** {person_name}"
        if also_called:
            context += f" (also called {also_called})"
        context += f"\n**Gender:** {gender}"
        if verse_count > 0:
            context += f"\n**Mentioned in:** {verse_count} verses"
        
        return f"""You are a Bible trivia expert. Generate a multiple-choice question about this biblical figure.

{context}
**Theme:** {theme}
**Difficulty:** {difficulty}

**Requirements:**
- Question about who they were, what they did, their relationships, or their significance
- Create 1 correct answer + 3 plausible distractors
- Distractors should be other biblical figures from similar time periods or contexts
- Avoid questions requiring exact verse memorization
- Make it educational and interesting
- Focus on their story, character, or impact

**Output Format (JSON only, no markdown):**
{{
  "question": "Clear question about this person",
  "choices": ["Correct answer", "Distractor 1", "Distractor 2", "Distractor 3"],
  "correctIndex": 0,
  "explanation": "Brief explanation with biblical reference"
}}

The correct answer should be at index 0.

Generate the question now:"""
    
    def _build_generic_prompt(self, template_data: Dict, difficulty: str) -> str:
        """Fallback generic prompt."""
        theme = template_data['theme']
        
        return f"""Generate a Bible trivia question for the theme: {theme}

**Difficulty:** {difficulty}

**Requirements:**
- Focus on stories, characters, events (NOT verse numbers or book names)
- 1 correct + 3 plausible distractors
- Educational and engaging
- Output JSON only

{{
  "question": "Question text",
  "choices": ["Correct answer", "Distractor 1", "Distractor 2", "Distractor 3"],
  "correctIndex": 0,
  "explanation": "Brief explanation"
}}

The correct answer should be at index 0."""
