import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from src.database import NewsDatabase

@pytest.fixture
def db():
    return NewsDatabase(":memory:")

def test_insert_and_get_articles(db):
    article = {"title": "Test", "content": "This is a test article"}
    db.insert_article(article)
    articles = db.get_articles()
    assert len(articles) == 1
    assert articles[0]["title"] == "Test"
    assert articles[0]["content"] == "This is a test article"

# TODO: Implement test for search articles method
