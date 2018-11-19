import pandas as pd 

airquality = pd.read_csv('airquality.csv')

print(airquality.head())

airquality_melt = pd.melt(frame = airquality, id_vars=['Month', 'Day'])

airquality_melt_sec = pd.melt(frame = airquality, id_vars=['Month', 'Day'], var_name='measurement', value_name='reading')

print(airquality_melt.head())

print(airquality_melt_sec.head())