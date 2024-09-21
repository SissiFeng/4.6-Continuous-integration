import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from src.scraper import NewsScraper

def test_fetch_news():
    scraper = NewsScraper("https://example.com")
    news = scraper.fetch_news("technology")
    assert isinstance(news, list)
    assert len(news) > 0
    assert "title" in news[0]
    assert "content" in news[0]

# TODO: Implement test for search_news method
