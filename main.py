import yfinance as yf

def read_price_data(stock_symbol, start_date, end_date, interval):
    """Import price data from Yahoo Finance"""
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
    price_series = stock_data.loc[:, 'Adj Close']
    price_series = price_series.fillna(method='ffill')
    return price_series

def get_date_list(stock_symbol, start_date, end_date, interval):
    """Generate a list of trading dates"""
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
    date_list = stock_data.index
    return date_list
