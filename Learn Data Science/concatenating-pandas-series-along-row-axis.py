import pandas as pd

jan = pd.read_csv('D:\Library Data Science\sales\sales-jan-2015.csv', parse_dates=True, index_col='Date')

feb = pd.read_csv('D:\Library Data Science\sales\sales-feb-2015.csv', parse_dates=True, index_col='Date')

mar = pd.read_csv('D:\Library Data Science\sales\sales-mar-2015.csv', parse_dates=True, index_col='Date')

units = []

for month in [jan, feb, mar]:
    units.append(month['Units'])

quarter1 = pd.concat(units, axis='rows')

print(quarter1.loc['jan 27, 2015':'feb 2, 2015'])

print(quarter1.loc['feb 26, 2015':'mar 7, 2015'])