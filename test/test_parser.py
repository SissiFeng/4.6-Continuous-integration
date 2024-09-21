from src.parser import NewsParser

def test_parse_article():
    article = {
        "title": "Test Article",
        "content": "This is a test article content.",
        "category": "Test"
    }
    parsed = NewsParser.parse_article(article)
    assert parsed['title'] == article['title']
    assert parsed['content'] == article['content']
    assert parsed['category'] == article['category']
    assert parsed['word_count'] == 6

def test_summarize_article():
    article = {
        "content": "This is a very long article content that should be summarized to a shorter version."
    }
    summary = NewsParser.summarize_article(article, max_words=5)
    assert len(summary.split()) == 5
    assert summary.endswith('...')

def test_extract_keywords():
    article = {
        "content": "Python is a popular programming language. It is used for web development, data analysis, and artificial intelligence."
    }
    keywords = NewsParser.extract_keywords(article, num_keywords=3)
    assert len(keywords) == 3
    assert all(isinstance(keyword, str) for keyword in keywords)

def test_categorize_article():
    article = {
        "title": "New Python Release",
        "content": "Python 3.10 has been released with new features including structural pattern matching."
    }
    category = NewsParser.categorize_article(article)
    assert isinstance(category, str)
    assert len(category) > 0
