from Api.connector import fetch_data

def formater(comp):
    data = fetch_data(comp)
    if data == []:
        result = {"status": "error", "message": "No data found"}
        return result
    comp_name = data[0]['name']
    news_data = []
    for item in data:
        article_dict = {
            'Title': item['title_desc'],
            'AI Sentiment Label': item['sentiment_label'],
            'AI Sentiment Score': round(item['sentiment_score'],2)
        }
        news_data.append(article_dict)
    master_shell = {
        "ticker": comp,
        "company_name": comp_name,
        "total_articles": len(data),
        "articles": news_data
    }
    return master_shell