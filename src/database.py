import sqlite3
from typing import List, Dict

class NewsDatabase:
    def __init__(self, db_name: str):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        """Create the news articles table if it doesn't exist."""
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS articles
            (id INTEGER PRIMARY KEY, title TEXT, content TEXT)
        ''')
        self.conn.commit()

    def insert_article(self, article: Dict[str, str]):
        """Insert a new article into the database."""
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO articles (title, content) VALUES (?, ?)
        ''', (article['title'], article['content']))
        self.conn.commit()

    def get_articles(self) -> List[Dict[str, str]]:
        """Retrieve all articles from the database."""
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM articles')
        return [{"id": row[0], "title": row[1], "content": row[2]} for row in cursor.fetchall()]

    # TODO: Implement method to search articles in the database
