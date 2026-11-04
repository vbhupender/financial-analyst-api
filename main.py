from fastapi import FastAPI, HTTPException
import yfinance as ticker_stream

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Financial Analyst API Active", "version": "1.0 Live Data"}

@app.get("/stock/{ticker}")
def get_stock_data(ticker: str):
    ticker_upper = ticker.upper()
    
    try:
        # Connect to Yahoo Finance for the specified ticker
        stock = yf.Ticker(ticker_upper)
        
        # Fast history fetch for the most recent day's data
        todays_data = stock.history(period="1d")
        
        if todays_data.empty:
            raise HTTPException(status_code=404, detail=f"Ticker '{ticker_upper}' not found or has no recent data.")
            
        # Extract the latest closing price
        current_price = todays_data['Close'].iloc[-1]
        
        # Get general company information (like official name and market cap)
        info = stock.info
        company_name = info.get('longName', 'Unknown Company')
        market_cap = info.get('marketCap', 'N/A')
        currency = info.get('currency', 'USD')

        return {
            "ticker": ticker_upper,
            "company_name": company_name,
            "current_price": round(current_price, 2),
            "currency": currency,
            "market_cap": market_cap,
            "status": "Live Data Fetched"
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving data: {str(e)}")
