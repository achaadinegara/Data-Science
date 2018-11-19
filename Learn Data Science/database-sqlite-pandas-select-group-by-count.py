import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sqlalchemy import MetaData, Table, create_engine, select, func

metadata = MetaData()

engine = create_engine('postgresql+psycopg2://student:datacamp@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com:5432/census')
engine = create_engine('sqlite:///census.sqlite')

connection = engine.connect()
census = Table('census', metadata, autoload=True, autoload_with=engine)

stmt = select([census.columns.state, func.count(census.columns.age)])
stmt = stmt.group_by(census.columns.age)
results = connection.execute(stmt).fetchall()

print(results)

print(results[0].keys())