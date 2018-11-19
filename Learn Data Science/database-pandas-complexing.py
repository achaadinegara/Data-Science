from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///Chinook.sqlite')

df = pd.read_sql_query(
    'SELECT * FROM Employee WHERE EmployeeId >= 6 ORDER BY Birthdate', engine)

print(df.head())