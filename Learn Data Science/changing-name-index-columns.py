import pandas as pd

sales = pd.read_csv('D:\Library Data Science\sales.csv')

sales.index.name = 'MONTHS'
sales.columns.name = 'PRODUCTS'

print(sales)