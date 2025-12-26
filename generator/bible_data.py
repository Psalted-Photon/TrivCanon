# Bible data access layer
import sqlite3, json, random
from pathlib import Path
from typing import List, Dict, Optional

class BibleData:
    def __init__(self, data_dir: str):
        self.data_dir = Path(data_dir)
        db_path = self.data_dir / 'bible.db'
        self.conn = sqlite3.connect(str(db_path))
        self.conn.row_factory = sqlite3.Row
        
        with open(self.data_dir / 'people.json', 'r', encoding='utf-8') as f:
            self.people = json.load(f)
        with open(self.data_dir / 'places.json', 'r', encoding='utf-8') as f:
            self.places = json.load(f)
        with open(self.data_dir / 'events.json', 'r', encoding='utf-8') as f:
            self.events = json.load(f)
        
        self.verse_table = 'KJV_verses'
        self.books_table = 'KJV_books'
    
    def get_random_verse(self, book: Optional[str] = None, min_length: int = 50) -> Dict:
        if book:
            query = f"""
            SELECT b.name as book, v.chapter, v.verse, v.text
            FROM {self.verse_table} v
            JOIN {self.books_table} b ON v.book_id = b.id
            WHERE b.name = ? AND LENGTH(v.text) >= ?
            ORDER BY RANDOM() LIMIT 1
            """
            cursor = self.conn.execute(query, (book, min_length))
        else:
            query = f"""
            SELECT b.name as book, v.chapter, v.verse, v.text
            FROM {self.verse_table} v
            JOIN {self.books_table} b ON v.book_id = b.id
            WHERE LENGTH(v.text) >= ?
            ORDER BY RANDOM() LIMIT 1
            """
            cursor = self.conn.execute(query, (min_length,))
        
        row = cursor.fetchone()
        if row:
            return dict(row)
        
        query = f"""
        SELECT b.name as book, v.chapter, v.verse, v.text
        FROM {self.verse_table} v
        JOIN {self.books_table} b ON v.book_id = b.id
        ORDER BY RANDOM() LIMIT 1
        """
        return dict(self.conn.execute(query).fetchone())
    
    def get_all_books(self) -> List[str]:
        cursor = self.conn.execute(f"SELECT DISTINCT name FROM {self.books_table} ORDER BY id")
        return [row['name'] for row in cursor.fetchall()]
    
    def get_random_person(self, gender: Optional[str] = None) -> Optional[Dict]:
        # Handle nested 'fields' structure in theographic data
        candidates = []
        for p in self.people:
            fields = p.get('fields', {})
            if not gender or fields.get('gender') == gender:
                candidates.append(fields)
        return random.choice(candidates) if candidates else None
    
    def get_random_place(self) -> Optional[Dict]:
        return random.choice(self.places) if self.places else None
    
    def get_random_event(self) -> Optional[Dict]:
        return random.choice(self.events) if self.events else None
    
    def close(self):
        self.conn.close()
