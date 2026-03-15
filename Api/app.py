from fastapi import FastAPI, HTTPException
from Api.formater import formater

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to BlueScrape"}

@app.get("/intelligence/{ticker}")
async def intelligence(ticker):
    ticker = ticker.upper()
    comps = ['AAPL', 'NVDA', 'AMD']
    if ticker not in comps:
        raise HTTPException(status_code = 404, detail = "Company not found.")
    result = formater(ticker)
    return result