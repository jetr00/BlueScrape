import yfinance as yf
import time

def fin():
    ticker1 = "AAPL"
    ticker2 = "NVDA"
    ticker3 = "AMD"

    print("Downloading data...")
    data1 = yf.download(ticker1, start="2025-11-01", end="2025-12-24", progress=False)
    data2 = yf.download(ticker2, start="2025-11-01", end="2025-12-24", progress=False)
    data3 = yf.download(ticker3, start="2025-11-01", end="2025-12-24", progress=False)

    ls = [data1, data2, data3]

    print("Data downloaded!")
    return ls