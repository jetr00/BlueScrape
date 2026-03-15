import yfinance as yf
import time

def fin(comp):

    print("Downloading data...")
    data = yf.download(comp, start="2025-11-01", end="2025-12-24", progress=False)

    ls = [data]

    print("Data downloaded!")
    return ls