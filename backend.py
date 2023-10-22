import yfinance as yf
import json

def main():
    tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "BRK-A", "FB", "TSM", "NVDA", "JPM", "JNJ", "V", "PG", "UNH", "MA", "HD", "BAC", "INTC", "VZ", "DIS"]
    results = []
    
    for ticker in tickers:
        ticker_info = get_ticker(ticker)
        if ticker_info:
            results.append({
                "ticker": ticker,
                "name": ticker_info.get('shortName', 'N/A'),
                "currentPrice": ticker_info.get('currentPrice', 'N/A'),
                "marketCap": ticker_info.get('marketCap', 'N/A'),
                "revenue": ticker_info.get('totalRevenue', 'N/A'),
                "revenueGrowth": ticker_info.get('revenueGrowth', 'N/A'),
                "grossProfits": ticker_info.get('grossProfits', 'N/A'),
                "netIncome": ticker_info.get('netIncomeToCommon', 'N/A')
            })
        else:
            results.append({
                "ticker": ticker,
                "error": f"Unable to fetch data for the ticker: {ticker}"
            })
    
    return json.dumps(results)

def get_ticker(ticker):
    ticker = yf.Ticker(ticker)
    info_data = ticker.info
    return info_data

if __name__ == '__main__':
    print(main())
