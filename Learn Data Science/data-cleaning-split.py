import pandas as pd

ebola = pd.read_csv('ebola.csv')

ebola_melt = pd.melt(ebola, id_vars=['Date', 'Day'], var_name='type_country', value_name='counts')

ebola_melt['str_split'] = ebola_melt.type_country.str.split('_')
ebola_melt['type'] = ebola_melt.str_split.str.get(0)
# Create the 'country' column
ebola_melt['country'] = ebola_melt.str_split.str.get(1)

print(ebola_melt.head())

