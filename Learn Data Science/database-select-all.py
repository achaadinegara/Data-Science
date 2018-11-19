from sqlalchemy import MetaData, Table, create_engine, select

engine = create_engine('sqlite:///census.sqlite')

metadata = MetaData()

census = Table('census', metadata, autoload=True, autoload_with=engine)

connection = engine.connect()

stmt = select([census])

#stmt = 'SELECT * FROM census'

results = connection.execute(stmt).fetchall()

print(results[10:21])

first_row = results[0]

print(first_row)

print(first_row.keys())

print(first_row.state)