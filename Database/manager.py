import sqlite3

def init_db():
    con = sqlite3.connect('BLUESCRAPE.db')
    cursor = con.cursor()
    try:
        cursor.execute(""" CREATE TABLE IF NOT EXISTS companies (
                        id INTEGER PRIMARY KEY,
                        ticker TEXT UNIQUE,
                        name TEXT,
                        sector TEXT
                        )""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS articles (
                        id TEXT PRIMARY KEY,
                        company_id INTEGER, 
                        source TEXT,
                        title_desc TEXT,
                        url TEXT,
                        published_at DATETIME,
                        FOREIGN KEY (company_id) REFERENCES companies(id)
                        )""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS sentiment_analysis (
                        id INTEGER PRIMARY KEY,
                        article_id TEXT,
                        sentiment_score FLOAT,
                        sentiment_label TEXT,
                        model_version TEXT,
                        FOREIGN KEY (article_id) REFERENCES articles(id)
                       )""")
        con.commit()
        print("Tables initialized.")
    except Exception as e:
        print(f"Tables already exist. {e}")
    con.close()
    return con

def seed_comp():
    con = sqlite3.connect('BLUESCRAPE.db')
    cursor = con.cursor()
    tar_comp = [
        ('AAPL', 'Apple Inc.', 'Technology'),
        ('NVDA', 'NVIDIA Corporation', 'Technology'),
        ('AMD', 'Advanced Micro Devices', 'Technology')
    ]

    cursor.executemany(''' INSERT OR IGNORE INTO companies(ticker, name, sector)
                       VALUES(?, ?, ?)''', tar_comp)
    con.commit()
    con.close()

def save_res(dl):
    con = sqlite3.connect('BLUESCRAPE.db')
    cursor = con.cursor()
    for d in dl:
        cursor.execute('''INSERT OR IGNORE INTO articles(id, company_id, source, title_desc, url, published_at)
                        VALUES(?, ?, ?, ?, ?, ?)''',(
                            d['url'],
                            d.get('company_id', 1),
                            d.get('source', 'Uknown'),
                            d['title'],
                            d['url'],
                            d.get('date', None)
                            ))
        cursor.execute('''INSERT INTO sentiment_analysis (article_id, sentiment_score, sentiment_label, model_version)
                        VALUES (?, ?, ?, ?)''',(
                            d['url'],
                            d['sentiment_score'],
                            d['sentiment_label'],
                            'FinBERT-v1'
                        ))
    con.commit()
    con.close()
    print(f"Successs! Saved {len(dl)} items to the database.")