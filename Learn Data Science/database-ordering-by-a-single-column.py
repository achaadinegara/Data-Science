from sqlalchemy import MetaData, Table, create_engine, select 

metadata = MetaData()

engine = create_engine('sqlite:///census.sqlite')

connection = engine.connect()

census = Table('census', metadata, autoload=True, autoload_with=engine)

# Build a query to select the state column: stmt
stmt = select([census.columns.state, census.columns.sex])

# Order stmt by the state column
stmt = stmt.order_by(census.columns.state, census.columns.sex)

results = connection.execute(stmt).fetchall()

print(results[:10])