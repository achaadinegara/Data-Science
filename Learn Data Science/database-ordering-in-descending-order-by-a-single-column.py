from sqlalchemy import MetaData, Table, create_engine, select, desc

metadata = MetaData()

engine = create_engine('sqlite:///census.sqlite')

connection = engine.connect()

census = Table('census', metadata, autoload=True, autoload_with=engine)

# stmt = select([census.columns.state])

# rev_stmt = stmt.order_by(desc(census.columns.state))

# rev_results = connection.execute(rev_stmt).fetchall()

# print(rev_results[:20])

stmt =select([census.columns.state, census.columns.age])

stmt = stmt.order_by(census.columns.state, desc(census.columns.age))

results = connection.execute(stmt).fetchall()

print(results[:20])