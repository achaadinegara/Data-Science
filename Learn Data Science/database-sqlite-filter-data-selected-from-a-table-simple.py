from sqlalchemy import MetaData, Table, create_engine, select

metadata = MetaData()

engine = create_engine('sqlite:///census.sqlite')

connection = engine.connect()

census = Table('census', metadata, autoload=True, autoload_with=engine)

stmt = select([census])

stmt = stmt.where(census.columns.state == 'New York')

results = connection.execute(stmt).fetchall()

for result in results:
    print(result.age, result.sex, result.pop2008)

#buka aja hastagnya kalau perlu
#NO STATES COLUMN..

# stmt = stmt.where(census.columns.state.in_(states))

# for result in connection.execute(stmt):
#     print(result.state, result.pop2000)