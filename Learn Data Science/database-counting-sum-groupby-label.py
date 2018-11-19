from sqlalchemy import MetaData, Table, create_engine, select, desc, func

metadata = MetaData()

engine = create_engine('sqlite:///census.sqlite')

connection = engine.connect()

census = Table('census', metadata, autoload=True, autoload_with=engine)

pop2008_sum = func.sum(census.columns.pop2008).label('population')

stmt = select([census.columns.state, pop2008_sum])

stmt = stmt.group_by(census.columns.state)

results = connection.execute(stmt).fetchall()

print(results)

print(results[0].keys())