import pandas as pd

gdp = pd.read_csv('gdp_usa.csv', parse_dates=True, index_col='DATE')

post2008 = gdp.loc['2008':]

print(post2008.tail(8))

yearly = post2008.resample('A').last()

print(yearly)

yearly['growth'] = yearly.pct_change()*100

print(yearly)