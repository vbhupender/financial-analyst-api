
from fastapi import FastAPI

app = FastAPI()

# Our original Hello World endpoint
@app.get("/")
def read_root():
    return {"message": "Hello World", "status": "Financial Analyst API Active"}

# New Endpoint: Accepts a stock ticker symbol dynamically from the URL
@app.get("/stock/{ticker}")
def get_stock_placeholder(ticker: str):
    # Convert input to uppercase (e.g., aapl -> AAPL)
    ticker_upper = ticker.upper()
    
    return {
        "ticker": ticker_upper,
        "message": f"Placeholder data for {ticker_upper}",
        "status": "Ready to integrate live market data feed"
    }
