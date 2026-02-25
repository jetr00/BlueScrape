from transformers import pipeline

def get_model():
    if not hasattr(get_model, "finbert"):
        print("Loading FinBERT AI Model (this might take a moment)...")
        get_model.finbert = pipeline("sentiment-analysis", model="ProsusAI/finbert")
    return get_model.finbert

def analyze_sentiment(tl):
    if not tl:
        return []
    
    finbert = get_model()

    res = finbert(tl)

    if res != []:
        print('AI analyzation Completed.')
    else:
        print('AI Analyzation Empty.')
    return res