from typing import List, Dict
from .mock_data import get_mock_news

class NewsScraper:
    def __init__(self):
        self.news_data = get_mock_news()

    def fetch_news(self, category: str = None) -> List[Dict[str, str]]:
        """Fetch news articles, optionally filtered by category."""
        if category:
            return [news for news in self.news_data if news['category'].lower() == category.lower()]
        return self.news_data

    def search_news(self, query: str) -> List[Dict[str, str]]:
        """Search for news articles based on a query."""
        return [news for news in self.news_data if query.lower() in news['title'].lower() or query.lower() in news['content'].lower()]

    # TODO: Implement a method to get the latest n news articles
    def get_latest_news(self, n: int) -> List[Dict[str, str]]:
        pass

    # TODO: Implement a method to get news by ID
    def get_news_by_id(self, news_id: int) -> Dict[str, str]:
        pass
