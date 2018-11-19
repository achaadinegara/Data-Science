import pandas as pd

tips = pd.read_csv('tips.csv')

tips['total_bill'] = pd.to_numeric(tips['total_bill'], errors='coerce')

tips['tip'] = pd.to_numeric(tips['tip'], errors='coerce')
print(tips.info())