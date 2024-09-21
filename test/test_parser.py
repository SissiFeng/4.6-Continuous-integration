import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.parser import NewsParser

def test_parse_article():
    html = "<html><head><title>Test Article</title></head><body>Content</body></html>"
    article = NewsParser.parse_article(html)
    assert article["title"] == "Test Article"
    assert "content" in article

# TODO: Implement test for extract_metadata method
