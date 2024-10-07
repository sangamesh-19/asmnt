import feedparser

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

# Example usage:
for feed in rss_feeds:
    articles = fetch_feed_data(feed)
    print(f"Fetched {len(articles)} articles from {feed}")
