import pandas as pd
import numpy as np

filename = 'pennsylvania2012_turnout.csv'

election = pd.read_csv(filename, index_col='county')

too_close = election['margin'] < 1
election.loc[too_close, 'winner'] = np.nan
print(election.info())
