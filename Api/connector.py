import sqlite3
from pathlib import Path
import sys

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

def fetch_data(comp):
    db_path = project_root / 'BLUESCRAPE.db'
    con = sqlite3.connect(db_path)
    con.row_factory = sqlite3.Row
    cursor = con.cursor()
    try:
        print("Fetching...")
        selection = cursor.execute('''SELECT companies.name, articles.title_desc, 
                                    sentiment_analysis.sentiment_label, sentiment_analysis.sentiment_score
                                    FROM companies JOIN articles ON companies.id = articles.company_id
                                    JOIN sentiment_analysis ON articles.id = sentiment_analysis.article_id
                                    WHERE companies.ticker = ?''', (comp,)).fetchall()
        print("Data Fetched!")
    except Exception as e:
        print(f"Database error: {e}")
        selection = []
    con.close()
    return selection