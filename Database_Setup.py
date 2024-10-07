from sqlalchemy import create_engine, Column, String, DateTime, Text, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import feedparser

# Define the declarative base
Base = declarative_base()

# Define the article table
class NewsArticle(Base):
    __tablename__ = 'news_articles'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(Text)
    pub_date = Column(DateTime)
    link = Column(String, unique=True)
    source = Column(String)
    category = Column(String, default="Uncategorized")

# Initialize the database
engine = create_engine('postgresql://username:password@localhost/newsdb')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Save an article
def save_article(article_data):
    # Check if the article already exists
    exists = session.query(NewsArticle).filter_by(link=article_data['link']).first()
    
    if not exists:
        new_article = NewsArticle(
            title=article_data['title'],
            content=article_data['content'],
            pub_date=datetime.strptime(article_data['pub_date'], '%a, %d %b %Y %H:%M:%S %Z'),
            link=article_data['link'],
            source=article_data['source']
        )
        session.add(new_article)
        session.commit()
        print(f"Saved article: {new_article.title}")

# List of RSS feeds
rss_feeds = [
    "http://rss.cnn.com/rss/cnn_topstories.rss",
    "http://qz.com/feed",
    "http://feeds.foxnews.com/foxnews/politics",
    "http://feeds.reuters.com/reuters/businessNews",
    "http://feeds.feedburner.com/NewshourWorld",
    "https://feeds.bbci.co.uk/news/world/asia/india/rss.xml"
]

def fetch_feed_data(feed_url):
    feed = feedparser.parse(feed_url)
    articles = []
    
    for entry in feed.entries:
        article = {
            "title": entry.title,
            "content": entry.summary,
            "pub_date": entry.published,
            "link": entry.link,
            "source": feed_url
        }
        articles.append(article)
    
    return articles

# Example usage
if __name__ == "__main__":
    for feed in rss_feeds:
        articles = fetch_feed_data(feed)
        print(f"Fetched {len(articles)} articles from {feed}")
        
        for article in articles:
            save_article(article)
