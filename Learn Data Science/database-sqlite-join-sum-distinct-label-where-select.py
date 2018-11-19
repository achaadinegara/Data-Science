import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sqlalchemy import MetaData, Table, create_engine, select, func, desc
from sqlalchemy import case, cast, Float

metadata = MetaData()
engine = create_engine(
     'mysql+pymysql://student:datacamp@courses.csrrinzqubik.us-east-1.rds.amazonaws.com:3306/census')

connection = engine.connect()
census = Table('census', metadata, autoload=True, autoload_with = engine)
state_fact = Table('state_fact', metadata, autoload=True, autoload_with=engine)

print(engine.table_names())

stmt = select([census.columns.pop2008,
               state_fact.columns.abbreviation])

result = connection.execute(stmt).fetchall()
print(result[0:10])
print('------------------------------------------------------------------')
stmt = select([func.sum(census.columns.pop2000)])
stmt = stmt.select_from(
    census.join(state_fact, census.columns.state == state_fact.columns.name))

stmt = stmt.where(
    state_fact.columns.census_division_name == 'East South Central'
)
results = connection.execute(stmt).scalar()

print(results)
print('------------------------------------------------------------------')
stmt = select([func.count(census.columns.state.distinct())])
distinct_state_count = connection.execute(stmt).scalar
print(distinct_state_count)
print('------------------------------------------------------------------')
stmt = select([census.columns.state, func.count(census.columns.age)])
stmt = stmt.group_by(census.columns.state)
results = connection.execute(stmt).fetchall()
print(results)
print(results[0].keys())
print('------------------------------------------------------------------')
pop2008_sum = func.sum(census.columns.pop2008).label('population')
stmt = select([census.columns.state, pop2008_sum])
stmt = stmt.group_by(census.columns.state)

results = connection.execute(stmt).fetchall()
print(results)
print(results[0].keys())
print('------------------------------------------------------------------')


