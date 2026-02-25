import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from Engine.config import get_settings
import httpx
import requests
import json

api = get_settings()

def apis():
    nak = api.news_api_key
    url = 'https://newsapi.org/v2/everything'

    queries = {
        'AAPL': 'apple AND (business OR stock OR finance OR revenue)',
        'NVDA': 'nvidia AND (business OR stock OR finance OR revenue)',
        'AMD': 'amd AND (business OR stock OR finance OR revenue)'
    }

    all_articles = []
    
    for ticker, query in queries.items():
        params = {
            'q': query,
            'domains': 'reuters.com,bloomberg.com,wsj.com,cnbc.com,marketwatch.com',
            'language': 'en',
            'sortBy': 'publishedAt',
            'apiKey': nak
        }
        res = requests.get(url, params=params)
        
        if res.status_code == 200:
            articles = res.json().get('articles', [])
            for art in articles:
                art['ticker'] = ticker
            all_articles.extend(articles)
        else:
            print(f"Warning: Failed to fetch news for {ticker}")
            
    return all_articles