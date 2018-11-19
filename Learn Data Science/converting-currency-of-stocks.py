import pandas as pd

sp500 = pd.read_csv('sp500.csv', parse_dates=True, index_col='Date')

print(sp500.head())

exchange = pd.read_csv('exchange.csv', parse_dates=True, index_col='Date')

print(exchange.head())

dollars = sp500[['Open', 'Close']]

print(dollars.head())

#convert
pounds = dollars.multiply(exchange['GBP/USD'], axis='rows')

print(pounds.head())