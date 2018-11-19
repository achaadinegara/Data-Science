from sqlalchemy import MetaData, create_engine

metadata = MetaData()
engine = create_engine('sqlite:///chapter5.sqlite')
connection = engine.connect()

from sqlalchemy import select, func, Table, Column, Integer, String

census = Table('census', metadata,
              Column('state', String(30)),
              Column('sex', String(1)),
              Column('age', Integer()),
              Column('pop2000', Integer()),
              Column('pop2008', Integer()),
              )

metadata.create_all(engine)

stmt = select([census.columns.sex,
        (func.sum(census.columns.pop2008 * census.columns.age)/
        func.sum(census.columns.pop2008)
        ).label('average_age')
    ])

stmt = stmt.group_by(census.columns.sex)

results = connection.execute(stmt).fetchall()
for result in results:
    print(result.sex, result.average_age)

