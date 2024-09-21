import sqlite3
from typing import List, Dict

class NewsDatabase:
    def __init__(self, db_name: str = ':memory:'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS articles
            (id INTEGER PRIMARY KEY, title TEXT, content TEXT, category TEXT)
        ''')
        self.conn.commit()

    def insert_article(self, article: Dict[str, str]):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO articles (title, content, category) VALUES (?, ?, ?)
        ''', (article['title'], article['content'], article['category']))
        self.conn.commit()

    def get_articles(self) -> List[Dict[str, str]]:
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM articles')
        return [{"id": row[0], "title": row[1], "content": row[2], "category": row[3]} for row in cursor.fetchall()]

    # TODO: Implement a method to update an existing article
    def update_article(self, article_id: int, updated_data: Dict[str, str]):
        pass

    # TODO: Implement a method to delete an article
    def delete_article(self, article_id: int):
        pass

    # TODO: Implement a method to get articles by category
    def get_articles_by_category(self, category: str) -> List[Dict[str, str]]:
        pass
