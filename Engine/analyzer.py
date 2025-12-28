from transformers import pipeline

def analyze_sentiment(tl):
    finbert = pipeline("sentiment-analysis", model="ProsusAI/finbert")
    res = finbert(tl)

    if res != []:
        print('AI analyzation Completed.')
    else:
        print('AI Analyzation Empty.')
    return res