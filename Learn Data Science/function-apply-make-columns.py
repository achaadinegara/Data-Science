import pandas as pd

weather = pd.read_csv('pittsburgh2013.csv')

def to_celcius(F):
    return 5/9*(F-32)

df_celcius = weather[['Mean TemperatureF', 'Mean Dew PointF']].apply(to_celcius)

df_celcius.columns = ['Mean TemperatureC', 'Mean Dew PointC']

print(df_celcius.head())