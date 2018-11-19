from sqlalchemy import MetaData, create_engine

metadata = MetaData()
engine = create_engine('sqlite:///chapter5.sqlite')
connection = engine.connect()

from sqlalchemy import Table, Column, String, Integer

census = Table('census', metadata,
              Column('state', String(30)),
              Column('sex', String(1)),
              Column('age', Integer()),
              Column('pop2000', Integer()),
              Column('pop2008', Integer()),
              )

metadata.create_all(engine)

import csv

f = open('census.csv', newline='')
csv_reader = csv.reader(f)


values_list = []

for row in csv_reader:
    data = {'state': row[0], 'sex': row[1],
     'age': row[2], 'pop2000': row[3],
     'pop2008': row[4]}
    values_list.append(data)

from sqlalchemy import insert

stmt = insert(census)

results = connection.execute(stmt, values_list)
print(results.rowcount)