import pandas as pd

names_1881 = pd.read_csv('names1881.csv')
names_1981 = pd.read_csv('names1981.csv')

names_1881['year'] = 1881
names_1981['year'] = 1891

combined_names = names_1881.append(names_1981, ignore_index=True)

print(names_1981.shape)
print(names_1881.shape)
print(combined_names.shape)

print(combined_names.loc[combined_names['name'] == 'Morgan'])    

#https://pandas.pydata.org/pandas-docs/stable/merging.html
#ignore_index: boolean, default False. Jika Benar, jangan gunakan nilai indeks pada sumbu penggabungan. 
# Sumbu yang dihasilkan akan diberi label 0, ..., n - 1. Ini berguna jika Anda menggabungkan objek di mana sumbu 
# penggabungan tidak memiliki informasi pengindeksan yang berarti. Perhatikan nilai indeks pada sumbu lain masih dihormati dalam gabung.