import pytest
from src.scraper import NewsScraper

@pytest.fixture
def scraper():
    return NewsScraper()

def test_fetch_news(scraper):
    news = scraper.fetch_news()
    assert isinstance(news, list)
    assert len(news) > 0
    assert all(isinstance(item, dict) for item in news)

def test_fetch_news_by_category(scraper):
    category = "Technology"
    news = scraper.fetch_news(category)
    assert all(item['category'] == category for item in news)

def test_search_news(scraper):
    query = "Python"
    results = scraper.search_news(query)
    assert all(query.lower() in item['title'].lower() or query.lower() in item['content'].lower() for item in results)

def test_get_latest_news(scraper):
    n = 3
    latest_news = scraper.get_latest_news(n)
    assert len(latest_news) == n
    # Check if the returned news are sorted by id in descending order
    assert all(latest_news[i]['id'] > latest_news[i+1]['id'] for i in range(len(latest_news)-1))
    # Check if the returned news are a subset of all news
    all_news = scraper.fetch_news()
    assert all(news in all_news for news in latest_news)

def test_get_news_by_id(scraper):
    news_id = 1
    article = scraper.get_news_by_id(news_id)
    assert article['id'] == news_id
