import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('auto mpg.csv')

cols = ['weight', 'mpg']

df[cols].plot(kind='box', subplots=True)

plt.show()