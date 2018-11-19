import pandas as pd

sales = pd.read_csv('D:\Library Data Science\sales.csv')

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

sales.index = months
print(sales)