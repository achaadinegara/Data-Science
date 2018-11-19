"""
Congratulations on executing your first SQL query! Now you're going to figure ou
how to customize your query in order to:
-Select specified columns from a table;
-Select a specified number of rows;
-Import column names from the database table.
"""
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///Chinook.sqlite')

with engine.connect() as con:
    rs = con.execute('SELECT LastName, Title FROM Employee')
    df = pd.DataFrame(rs.fetchmany(size=3))
    df.columns = rs.keys()

print(len(df))

print(df.head())