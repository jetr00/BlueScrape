BlueScrape is a Python-based tool designed to scrape and aggregate data efficiently. This project uses external APIs to fetch information and process it locally.

## 📋 Prerequisites

Before running the program, ensure you have the following installed on your system:
* Python 3.13.5
* Git
* Pip (Python package manager)

---

An end-to-end data pipeline that fetches real-time financial news, filters out noise using advanced BM25 ranking, and analyzes market sentiment using a fine-tuned NLP model (FinBERT). 

## 🚀 Architecture Overview

This system is built as a modular, production-ready backend intelligence engine:
1. **Data Ingestion (`yfinance`, `NewsAPI`):** Fetches historical stock data and live financial news concurrently for targeted tickers (AAPL, NVDA, AMD).
2. **Information Retrieval (`BM25`):** Acts as a high-performance search engine to filter out irrelevant news articles before processing, saving compute power.
3. **AI Intelligence (`Transformers`, `FinBERT`):** Uses Hugging Face's pipeline (optimized with Lazy/Singleton loading) to score the financial sentiment of the filtered text.
4. **Relational Storage (`SQLite`):** Automatically maps and stores the structured intelligence (companies, articles, and sentiment scores) into normalized database tables.

## 🛠️ Tech Stack
* **Language:** Python 3.11+
* **AI/NLP:** Hugging Face `transformers` (ProsusAI/finbert), `PyTorch`
* **Search/Ranking:** `bm25_fusion`
* **Data Validation:** `pydantic_settings`
* **Database:** SQLite3 (with automated schema initialization)

## 📁 Project Structure
```text
BlueScrape/
├── Database/
│   └── manager.py       # Database connection, schema init, and inserts
├── Engine/
│   ├── analyzer.py      # AI model lazy-loading and sentiment scoring
│   ├── config.py        # Pydantic environment validation
│   ├── fetcher.py       # Stock data retrieval (yfinance)
│   ├── filtering.py     # BM25 text corpus filtering
│   └── models.py        # News API integration
├── Main/
│   └── main.py          # Pipeline orchestrator
├── .env                 # API Keys (Ignored by Git)
├── .gitignore           # Security and cache shielding
└── requirements.txt     # Project dependencies

⚙️ How to Run Locally
1. Clone the repository
Bash

git clone git@github.com:jetr00/BlueScrape.git
cd BlueScrape

2. Install Dependencies

It is recommended to use a virtual environment.
Bash

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt

3. Environment Variables

Create a .env file in the root directory and add your API credentials:
Code snippet

NEWS_API_KEY=your_actual_api_key_here

4. Run the Pipeline
Bash

python Main/main.py

Upon running, the engine will automatically initialize the database, fetch market news, run the AI sentiment analysis, and securely save the intelligence to BLUESCRAPE.db.
```

🧠 Technical Highlights

    Singleton AI Loading: Prevented memory-leaks and multiprocessing crashes by implementing a Singleton design pattern for the Hugging Face pipeline.

    Environment Gatekeeping: Used Pydantic to strictly validate configuration settings before runtime, preventing system crashes due to missing or malformed keys.

    Database Normalization: Designed a multi-table relational schema ensuring referential integrity between companies, articles, and sentiment_analysis.

### Author

    jetr00 - John Choriatellis
