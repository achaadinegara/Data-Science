#finding file in pattern
import glob
import pandas as pd

pattern = '*.csv'
csv_files = glob.glob(pattern)
#print(csv_files)
csv2 = pd.read_csv(csv_files[1])
#print(csv2.head())


#iterating and concatenating
frames = []

for csv in csv_files:
    df = pd.read_csv(csv)
    frames.append(df)

uber = pd.concat(frames)   
print(uber.shape) 
print(uber.head())