from Engine.config import get_settings
import httpx
import requests
import json

api = get_settings()

def apis():
    nak = api.news_api_key
    url = 'https://newsapi.org/v2/everything'
    apple_art = {
        'q' : 'apple AND (business OR stock OR finance OR revenue)',
        'domains': 'reuters.com,bloomberg.com,wsj.com,cnbc.com,marketwatch.com',
        'language' : 'en',
        'sortBy': 'publishedAt',
        'apiKey' : nak
        }

    nvidia_art = {
        'q' : 'nvidia AND (business OR stock OR finance OR revenue)',
        'domains': 'reuters.com,bloomberg.com,wsj.com,cnbc.com,marketwatch.com',
        'language' : 'en',
        'sortBy': 'publishedAt',
        'apiKey' : nak
        }

    amd_art = {
        'q' : 'amd AND (business OR stock OR finance OR revenue)',
        'domains': 'reuters.com,bloomberg.com,wsj.com,cnbc.com,marketwatch.com',
        'language' : 'en',
        'sortBy': 'publishedAt',
        'apiKey' : nak
        }

    res1 = requests.get(url, params=apple_art)
    res2 = requests.get(url, params=nvidia_art)
    res3 = requests.get(url, params=amd_art)
    if res1.status_code == 200 and res2.status_code == 200 and res3.status_code == 200:
        all_articles = (
            res1.json().get('articles', []) +
            res2.json().get('articles', []) +
            res3.json().get('articles', [])
        )
        return all_articles
    return []