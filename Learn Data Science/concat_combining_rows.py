import pandas as pd

uber1 = pd.read_csv('uber1.csv')
uber2 = pd.read_csv('uber2.csv')
uber3 = pd.read_csv('uber3.csv')


#combining columns
row_concat =  pd.concat([uber1, uber2, uber3], axis=1)

print(row_concat.head())