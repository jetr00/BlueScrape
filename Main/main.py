import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from Database.manager import init_db, save_res, seed_comp
from Engine.fetcher import fin
from Engine.analyzer import analyze_sentiment
from Engine.config import get_settings
from Engine.filtering import filt
from Engine.models import apis

def main():
    get_settings()

    init_db()
    seed_comp()

    company_ids = {'AAPL': 1, 'NVDA': 2, 'AMD': 3}

    ls = fin()
    news = apis()

    articles = filt(news)

    texts = [a.get('text', '') for a in articles]

    ai_res = analyze_sentiment(texts)

    ml = []
    for article, sentiment in zip(articles, ai_res):
        meta = article.get('metadata', {})
        ticker = meta.get('ticker', 'AAPL')

        merged_item = {
            'url': meta.get('url', 'Unknown URL'),
            'title': article.get('text', 'No Title'),
            'source': meta.get('source', {}).get('name', 'Unknown'),
            'date': meta.get('publishedAt', None),
            'company_id': company_ids.get(ticker, 1),
            'sentiment_label': sentiment['label'],
            'sentiment_score': sentiment['score']
        }
        ml.append(merged_item)

    save_res(ml)
    print('News and Sentiment saved successfully.')

if __name__ == "__main__":
    main()