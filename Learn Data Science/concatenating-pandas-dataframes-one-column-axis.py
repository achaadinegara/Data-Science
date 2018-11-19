import pandas as pd

weather_max = pd.read_csv('quartely_max_temp.csv')
weather_mean = pd.read_csv('monthly_mean_temp.csv')

weather = pd.concat([weather_max, weather_mean], axis=1)

print(weather)