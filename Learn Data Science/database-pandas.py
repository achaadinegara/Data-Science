from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///Chinook.sqlite')

df = pd.read_sql_query('SELECT * FROM Album', engine)

print(df.head())

#Open engine in context manager

with engine.connect() as con:
    rs = con.execute('SELECT * FROM Album')
    df1 = pd.DataFrame(rs.fetchall())
    df1.columns = rs.keys()

print(df.equals(df1))