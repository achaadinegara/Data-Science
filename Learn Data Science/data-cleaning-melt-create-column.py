import pandas as pd

tb = pd.read_csv('tb.csv')

tb_melt = pd.melt(frame=tb, id_vars=['country', 'year'])

tb_melt['gender'] = tb_melt.variable.str[0]

tb_melt['age_group'] = tb_melt.variable.str[1:]

print(tb_melt.head())