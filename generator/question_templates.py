"""Question generation templates mapped to themes."""

import random
from typing import Dict
from bible_data import BibleData

class QuestionTemplates:
    """Generate question templates using Bible data, mapped to themes."""
    
    def __init__(self, bible_data: BibleData):
        self.bible = bible_data
        
        # Map themes to generation methods
        self.theme_generators = {
            "Miracles": self.generate_miracle_question,
            "Prophets": self.generate_prophet_question,
            "Apostles": self.generate_apostle_question,
            "Kings & Rulers": self.generate_king_question,
            "Women of Faith": self.generate_women_question,
            "Battles & Conquests": self.generate_battle_question,
            "Parables & Teachings": self.generate_parable_question,
            "Creation & Origins": self.generate_creation_question,
            "Prophecy & End Times": self.generate_prophecy_question,
            "Journeys & Exile": self.generate_journey_question,
            "Festivals & Customs": self.generate_festival_question,
            "Wisdom & Psalms": self.generate_wisdom_question
        }
    
    def generate_for_theme(self, theme: str) -> Dict:
        """Generate a question template for a specific theme."""
        generator = self.theme_generators.get(theme)
        if generator:
            return generator()
        else:
            # Fallback to generic verse question
            return self.generate_generic_verse_question(theme)
    
    def generate_miracle_question(self) -> Dict:
        """Generate question about miracles."""
        # Books with many miracles
        miracle_books = ['Matthew', 'Mark', 'Luke', 'John', 'Acts', 'Exodus']
        available_books = [b for b in miracle_books if b in self.bible.get_all_books()]
        
        if available_books:
            book = random.choice(available_books)
            verse = self.bible.get_random_verse(book, min_length=60)
        else:
            verse = self.bible.get_random_verse(min_length=60)
        
        return {
            'template': 'verse_context',
            'verse': verse,
            'theme': 'Miracles',
            'prompt_hint': 'miracle, healing, or supernatural event'
        }
    
    def generate_prophet_question(self) -> Dict:
        """Generate question about prophets."""
        prophet_books = ['Isaiah', 'Jeremiah', 'Ezekiel', 'Daniel', 'Hosea', 
                        'Joel', 'Amos', 'Jonah', 'Micah', 'Nahum', 'Malachi']
        available_books = [b for b in prophet_books if b in self.bible.get_all_books()]
        
        if available_books:
            book = random.choice(available_books)
            verse = self.bible.get_random_verse(book)
        else:
            verse = self.bible.get_random_verse()
        
        return {
            'template': 'verse_context',
            'verse': verse,
            'theme': 'Prophets',
            'prompt_hint': 'prophecy, prophet, or divine message'
        }
    
    def generate_apostle_question(self) -> Dict:
        """Generate question about apostles."""
        apostle_books = ['Matthew', 'Mark', 'Luke', 'John', 'Acts', 
                        'Romans', '1 Corinthians', '2 Corinthians', 'Galatians']
        available_books = [b for b in apostle_books if b in self.bible.get_all_books()]
        
        if available_books:
            book = random.choice(available_books)
            verse = self.bible.get_random_verse(book)
        else:
            verse = self.bible.get_random_verse()
        
        return {
            'template': 'verse_context',
            'verse': verse,
            'theme': 'Apostles',
            'prompt_hint': 'apostle, disciple, or early church leader'
        }
    
    def generate_king_question(self) -> Dict:
        """Generate question about kings and rulers."""
        king_books = ['1 Samuel', '2 Samuel', '1 Kings', '2 Kings', 
                     '1 Chronicles', '2 Chronicles', 'Daniel', 'Esther']
        available_books = [b for b in king_books if b in self.bible.get_all_books()]
        
        if available_books:
            book = random.choice(available_books)
            verse = self.bible.get_random_verse(book)
        else:
            verse = self.bible.get_random_verse()
        
        return {
            'template': 'verse_context',
            'verse': verse,
            'theme': 'Kings & Rulers',
            'prompt_hint': 'king, ruler, or royal decree'
        }
    
    def generate_women_question(self) -> Dict:
        """Generate question about women of faith."""
        # Try to get a female person from theographic data
        women = [p for p in self.bible.people if p.get('gender') == 'Female']
        
        if women and random.random() < 0.3:  # 30% chance to use person data
            person = random.choice(women)
            return {
                'template': 'person_relationship',
                'person': person,
                'theme': 'Women of Faith',
                'prompt_hint': 'biblical woman, her story or significance'
            }
        else:
            # Fallback to verse from books featuring women
            women_books = ['Ruth', 'Esther', 'Luke', 'Acts', 'Judges']
            available_books = [b for b in women_books if b in self.bible.get_all_books()]
            
            if available_books:
                book = random.choice(available_books)
                verse = self.bible.get_random_verse(book)
            else:
                verse = self.bible.get_random_verse()
            
            return {
                'template': 'verse_context',
                'verse': verse,
                'theme': 'Women of Faith',
                'prompt_hint': 'woman, faithful woman, or female biblical figure'
            }
    
    def generate_battle_question(self) -> Dict:
        """Generate question about battles and conquests."""
        battle_books = ['Joshua', 'Judges', '1 Samuel', '2 Samuel', 
                       '1 Kings', '2 Kings', 'Revelation', '1 Chronicles']
        available_books = [b for b in battle_books if b in self.bible.get_all_books()]
        
        if available_books:
            book = random.choice(available_books)
            verse = self.bible.get_random_verse(book)
        else:
            verse = self.bible.get_random_verse()
        
        return {
            'template': 'verse_context',
            'verse': verse,
            'theme': 'Battles & Conquests',
            'prompt_hint': 'battle, war, conquest, or military victory'
        }
    
    def generate_parable_question(self) -> Dict:
        """Generate question about parables and teachings."""
        parable_books = ['Matthew', 'Mark', 'Luke']
        available_books = [b for b in parable_books if b in self.bible.get_all_books()]
        
        if available_books:
            book = random.choice(available_books)
            verse = self.bible.get_random_verse(book, min_length=70)
        else:
            verse = self.bible.get_random_verse(min_length=70)
        
        return {
            'template': 'verse_context',
            'verse': verse,
            'theme': 'Parables & Teachings',
            'prompt_hint': 'parable, teaching, or lesson from Jesus'
        }
    
    def generate_creation_question(self) -> Dict:
        """Generate question about creation and origins."""
        # Focus on Genesis 1-11
        verse = self.bible.get_random_verse('Genesis', min_length=40)
        
        # Try to get from early chapters
        if verse and verse.get('chapter', 100) > 11:
            # Retry a few times to get early chapters
            for _ in range(3):
                retry_verse = self.bible.get_random_verse('Genesis', min_length=40)
                if retry_verse and retry_verse.get('chapter', 100) <= 11:
                    verse = retry_verse
                    break
        
        return {
            'template': 'verse_context',
            'verse': verse,
            'theme': 'Creation & Origins',
            'prompt_hint': 'creation, early humanity, or origins'
        }
    
    def generate_prophecy_question(self) -> Dict:
        """Generate question about prophecy and end times."""
        prophecy_books = ['Daniel', 'Revelation', 'Isaiah', 'Ezekiel', 'Zechariah']
        available_books = [b for b in prophecy_books if b in self.bible.get_all_books()]
        
        if available_books:
            book = random.choice(available_books)
            verse = self.bible.get_random_verse(book)
        else:
            verse = self.bible.get_random_verse()
        
        return {
            'template': 'verse_context',
            'verse': verse,
            'theme': 'Prophecy & End Times',
            'prompt_hint': 'prophecy, end times, or future revelation'
        }
    
    def generate_journey_question(self) -> Dict:
        """Generate question about journeys and exile."""
        journey_books = ['Exodus', 'Numbers', 'Deuteronomy', 'Ezra', 'Nehemiah', 'Acts']
        available_books = [b for b in journey_books if b in self.bible.get_all_books()]
        
        if available_books:
            book = random.choice(available_books)
            verse = self.bible.get_random_verse(book)
        else:
            verse = self.bible.get_random_verse()
        
        return {
            'template': 'verse_context',
            'verse': verse,
            'theme': 'Journeys & Exile',
            'prompt_hint': 'journey, exile, travel, or pilgrimage'
        }
    
    def generate_festival_question(self) -> Dict:
        """Generate question about festivals and customs."""
        festival_books = ['Leviticus', 'Deuteronomy', 'Exodus', 'John', 'Acts']
        available_books = [b for b in festival_books if b in self.bible.get_all_books()]
        
        if available_books:
            book = random.choice(available_books)
            verse = self.bible.get_random_verse(book)
        else:
            verse = self.bible.get_random_verse()
        
        return {
            'template': 'verse_context',
            'verse': verse,
            'theme': 'Festivals & Customs',
            'prompt_hint': 'festival, custom, ceremony, or Jewish tradition'
        }
    
    def generate_wisdom_question(self) -> Dict:
        """Generate question about wisdom and psalms."""
        wisdom_books = ['Psalms', 'Proverbs', 'Ecclesiastes', 'Job', 'Song of Solomon']
        available_books = [b for b in wisdom_books if b in self.bible.get_all_books()]
        
        if available_books:
            book = random.choice(available_books)
            verse = self.bible.get_random_verse(book, min_length=40)
        else:
            verse = self.bible.get_random_verse(min_length=40)
        
        return {
            'template': 'verse_context',
            'verse': verse,
            'theme': 'Wisdom & Psalms',
            'prompt_hint': 'wisdom, proverb, psalm, or poetic teaching'
        }
    
    def generate_generic_verse_question(self, theme: str) -> Dict:
        """Fallback: generate question from random verse."""
        verse = self.bible.get_random_verse()
        return {
            'template': 'verse_context',
            'verse': verse,
            'theme': theme,
            'prompt_hint': 'biblical knowledge'
        }
