import pandas as pd

jan = pd.read_csv('D:\Library Data Science\sales\sales-jan-2015.csv', parse_dates=True, index_col='Date')

feb = pd.read_csv('D:\Library Data Science\sales\sales-feb-2015.csv', parse_dates=True, index_col='Date')

mar = pd.read_csv('D:\Library Data Science\sales\sales-mar-2015.csv', parse_dates=True, index_col='Date')

jan_units = jan['Units']

feb_units = feb['Units']

mar_units = mar['Units']

quarter1 = jan_units.append(feb_units).append(mar_units)

print(quarter1.loc['jan 27, 2015':'feb 2, 2015'])

print(quarter1.loc['feb 26, 2015':'mar 7, 2015'])

print(quarter1.sum())