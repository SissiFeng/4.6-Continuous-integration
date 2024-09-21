import pytest
from src.database import NewsDatabase

@pytest.fixture
def db():
    return NewsDatabase(':memory:')

def test_insert_and_get_articles(db):
    article = {
        "title": "Test Article",
        "content": "This is a test article content.",
        "category": "Test"
    }
    db.insert_article(article)
    articles = db.get_articles()
    assert len(articles) == 1
    assert articles[0]['title'] == article['title']
    assert articles[0]['content'] == article['content']
    assert articles[0]['category'] == article['category']

def test_update_article(db):
    article = {
        "title": "Original Title",
        "content": "Original content",
        "category": "Original"
    }
    db.insert_article(article)
    articles = db.get_articles()
    article_id = articles[0]['id']
    
    updated_data = {
        "title": "Updated Title",
        "content": "Updated content",
        "category": "Updated"
    }
    db.update_article(article_id, updated_data)
    
    updated_articles = db.get_articles()
    assert updated_articles[0]['title'] == updated_data['title']
    assert updated_articles[0]['content'] == updated_data['content']
    assert updated_articles[0]['category'] == updated_data['category']

def test_delete_article(db):
    article = {
        "title": "To Be Deleted",
        "content": "This article will be deleted.",
        "category": "Test"
    }
    db.insert_article(article)
    articles = db.get_articles()
    article_id = articles[0]['id']
    
    db.delete_article(article_id)
    
    remaining_articles = db.get_articles()
    assert len(remaining_articles) == 0

def test_get_articles_by_category(db):
    articles = [
        {"title": "Tech News 1", "content": "Content 1", "category": "Technology"},
        {"title": "Sports News", "content": "Content 2", "category": "Sports"},
        {"title": "Tech News 2", "content": "Content 3", "category": "Technology"}
    ]
    for article in articles:
        db.insert_article(article)
    
    tech_articles = db.get_articles_by_category("Technology")
    assert len(tech_articles) == 2
    assert all(article['category'] == "Technology" for article in tech_articles)
