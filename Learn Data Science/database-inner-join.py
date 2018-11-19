import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///Chinook.sqlite')

df = pd.read_sql_query(
    'SELECT * FROM PlaylistTrack INNER JOIN Track on PlaylistTrack.TrackId = Track.TrackID WHERE Milliseconds < 250000', engine)

print(df.head())
