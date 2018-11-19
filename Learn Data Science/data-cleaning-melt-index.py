import pandas as pd
users = pd.read_csv('users.csv')

skinny = pd.melt(users, id_vars=['weekday','city'])

print(skinny)