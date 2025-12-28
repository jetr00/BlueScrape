import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from Database.manager import init_db
from Database.manager import save_res
from Database.manager import seed_comp
from Engine.fetcher import fin
from Engine.analyzer import analyze_sentiment
from Engine.config import get_settings
from Engine.filtering import filt
from Engine.models import apis

def main():
    get_settings()
    ls = fin()
    news = apis()
    articles = filt(news)
    texts = [a['text'] for a in articles]
    ai_res = analyze_sentiment(texts)
    init_db()
    seed_comp()
    ml = []

    for article, sentiment in zip(articles, ai_res):
        merged_item = {
            'url': article['url'],
            'title': article['text'],
            'sentiment_label': sentiment['label'],
            'sentiment_score': sentiment['score']
        }
        ml.append(merged_item)
    save_res(ml)
    print('News and Sentiment saved successfully.')

if __name__ == "__main__":
    main()