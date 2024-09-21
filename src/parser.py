from typing import Dict, List

class NewsParser:
    @staticmethod
    def parse_article(article: Dict[str, str]) -> Dict[str, str]:
        """Parse an article and extract relevant information."""
        return {
            "title": article['title'],
            "content": article['content'],
            "category": article['category'],
            "word_count": len(article['content'].split())
        }

    @staticmethod
    def summarize_article(article: Dict[str, str], max_words: int = 30) -> str:
        """Create a summary of the article content."""
        words = article['content'].split()
        return ' '.join(words[:max_words]) + ('...' if len(words) > max_words else '')

    # TODO: Implement a method to extract keywords from the article
    @staticmethod
    def extract_keywords(article: Dict[str, str], num_keywords: int = 5) -> List[str]:
        pass

    # TODO: Implement a method to categorize the article based on its content
    @staticmethod
    def categorize_article(article: Dict[str, str]) -> str:
        pass
