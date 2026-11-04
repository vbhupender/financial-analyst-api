
from fastapi import FastAPI, HTTPException
import yfinance as ticker_stream


app = FastAPI(title="Financial Analyst API")

def patch_ticker(ticker: str) -> str:
    """
    Smart Ticker Patching: Automatically formats raw symbols for the Indian Market (NSE).
    If a user types 'TCS', it becomes 'TCS.NS'. If they type 'AAPL', it stays 'AAPL'.
    """
    cleaned_ticker = ticker.strip().upper()

    # List of common US/Global tickers to skip patching, or check if it already has an extension
    if "." in cleaned_ticker:
      return cleaned_ticker

        # Example logic: Assume 3+ character uppercase strings without a dot are Indian equities 
        # (You can customize this list or logic as your API grows!)
    us_benchmark_tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "NVDA", "META"]

    if cleaned_ticker not in us_benchmark_tickers:
        return f"{cleaned_ticker}.NS"
    
    return cleaned_ticker

# --- API Endpoints ---
@app.get("/")
def read_root():
    return {"message": "Financial Ananlyst is up and running!"}

@app.get("/stock/{ticker}")
def get_live_stock(ticker: str):
    # Apply the smart ticker patch
    patched_symbol = patch_ticker(ticker)
     
    try:
        stock = ticker_stream.Ticker(patched_symbol)
        info = stock.info

        # Verify if yfinance returns an empty or invalid dictionary
        if not info or not isinstance(info, dict):
            raise HTTPException(status_code=404, detail=f"Ticker data for'{patched_symbol}' not found.")

        # Safely fetch prices using multiple fallback keys that yfinance uses.
        current_price = (
            info.get("currentPrice") 
            or info.get("regularMarketPrice")
            or info.get("open")
        )

        if not current_price:
            raise HTTPException(status_code=404, detail=f"Price metrics for'{patched_symbol}' are unavailable")
        
        return {
            "requested_ticker": ticker,
            "resolved_ticker": patched_symbol,
            "company_name": info.get("longName", "N/A"),
            "current_price": current_price,
            "currency": info.get("currency", "USD" if ".NS" not in patched_symbol else "INR"),
            "market_cap": info.get("marketCap", "N/A")
        }
    except Exception as he:
        raise he
    except Exception as e:
        # This will send the actual error message back to swagger to help us debug
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/stock{ticker}/trends")
def get_stock_trends(ticker: str):
    # Historical Trends Endpoint: Fetches last 30 days of closing price.
    patched_symbol = patch_ticker(ticker)

    try:
        stock = ticker_stream.Ticker(patched_symbol)
        
        #fetch 1 month of historical data at a daily interval
        history = stock.history(period="1mo", interval="1d")

        if history.empty:
            raise HTTPException(status_code=404, detail=f" No historical data found for {patched_symbol}")

        # Extract closing prices and map dates to strings
        trends_data = []
        for date, row in history.iterrows():
            trends_data.append({
                "date": date.strftime("%Y-%m-%d"),
                "close": round(row["Close"],2)
            })

        return {
            "ticker": patched_symbol,
            "period": "30_days",
            "data_points_count": len(trends_data),
            "price_history": trends_data
        
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    







