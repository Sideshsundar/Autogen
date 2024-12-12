# filename: stock_prices.py
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

#define the ticker symbol
tickerSymbols = ['NVDA', 'TSLA']

#create empty dataframe
stock_data = pd.DataFrame()

#fetch data on each ticker symbol
for ticker in tickerSymbols:
    data = yf.Ticker(ticker)
    #get historical market data
    hist = data.history(period="YTD")
    #add this data to the data frame, we will use Close price for plotting
    stock_data[ticker]=hist['Close']

#plot data
stock_data.plot(figsize=(10, 5))
plt.title("Stock Price change YTD")
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()