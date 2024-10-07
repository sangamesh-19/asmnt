import logging

logging.basicConfig(filename='news_collector.log', level=logging.INFO)

def log_message(message):
    logging.info(message)

def log_error(error):
    logging.error(error)
