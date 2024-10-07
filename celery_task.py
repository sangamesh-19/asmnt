from celery import Celery

# Celery instance
celery_app = Celery('news_collector', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

# Dummy category classification function
def classify_article(content):
    # Example logic for classifying an article based on content
    if 'technology' in content.lower():
        return 'Technology'
    elif 'politics' in content.lower():
        return 'Politics'
    elif 'sports' in content.lower():
        return 'Sports'
    else:
        return 'General'

# Dummy function to save the article (e.g., into a database)
def save_article(article):
    # Logic to save the article in the database
    # For example: save to a PostgreSQL or NoSQL database
    print(f"Saving article: {article['title']} in category: {article['category']}")
    # Assume the actual database save logic goes here

@celery_app.task
def process_article(article):
    # Classify the article and save it
    category = classify_article(article['content'])
    article['category'] = category
    save_article(article)
