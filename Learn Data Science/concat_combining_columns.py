import pandas as pd

ebola = pd.read_csv('ebola.csv')
status_country = pd.read_csv('ebola.csv')
ebola_melt = pd.melt(ebola, id_vars=['Date', 'Day'], var_name='type_country', value_name='counts')

ebola_tidy = pd.concat([ebola_melt, status_country], axis=1)

print(ebola_tidy.head())