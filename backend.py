import yfinance as yf

def main():
    tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "BRK-A", "FB", "TSM", "NVDA", "JPM", "JNJ", "V", "PG", "UNH", "MA", "HD", "BAC", "INTC", "VZ", "DIS"]
    
    for ticker in tickers:
        ticker_info = get_ticker(ticker)
        print(f"Ticker: {ticker}")
        if ticker_info:
            print("Ticker Name:", ticker_info.get('shortName', 'N/A'))
            print("Current Stock Price:", ticker_info.get('currentPrice', 'N/A'))
            print("Market Cap:", ticker_info.get('marketCap', 'N/A'))
            print("12-Month Revenue:", ticker_info.get('totalRevenue', 'N/A'))
            print("YoY Revenue Growth:", ticker_info.get('revenueGrowth', 'N/A'))
            print("Gross Profit (12-Month):", ticker_info.get('grossProfits', 'N/A'))
            print("Net Profit (12-Month):", ticker_info.get('netIncomeToCommon', 'N/A'))
        else:
            print(f"Unable to fetch data for the ticker: {ticker}")
        print("\n")

def get_ticker(ticker):
    ticker = yf.Ticker(ticker)
    info_data = ticker.info
    return info_data

if __name__ == '__main__':
    main()
