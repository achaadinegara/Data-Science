import pandas as pd
import numpy as np

filename = 'pennsylvania2012_turnout.csv'

election = pd.read_csv(filename, index_col='county')

high_turnout = election['turnout'] > 70

high_turnout_df = election[high_turnout]

print(high_turnout_df)


