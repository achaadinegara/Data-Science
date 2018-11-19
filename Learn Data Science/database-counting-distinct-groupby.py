from sqlalchemy import MetaData, Table, create_engine, select, desc, func

metadata = MetaData()

engine = create_engine('sqlite:///census.sqlite')

connection = engine.connect()

census = Table('census', metadata, autoload=True, autoload_with=engine)

# Build a query to count the distinct states values: stmt

stmt = select([func.count(census.columns.state.distinct())])

distinct_state_count = connection.execute(stmt).scalar()

print(distinct_state_count)

stmt = select([census.columns.state, func.count(census.columns.age)])

stmt = stmt.group_by(census.columns.state)

results = connection.execute(stmt).fetchall()

print(results)
