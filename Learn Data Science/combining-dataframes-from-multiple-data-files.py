import pandas as pd

bronze = pd.read_csv('Bronze.csv')
silver = pd.read_csv('Silver.csv')
gold = pd.read_csv('Gold.csv')

print(gold.head())
print('--------------------------------------------------')

medals = gold.copy()
new_labels = ['NOC', 'Country', 'Gold']
medals.columns = new_labels
medals['Silver'] = silver['Total']
medals['Bronze'] = bronze['Total']


print(medals.head())