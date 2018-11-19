from sqlalchemy import MetaData, Table, create_engine, select, and_, or_

metadata = MetaData()

engine = create_engine('sqlite:///census.sqlite')

connection = engine.connect()

census = Table('census', metadata, autoload=True, autoload_with=engine)

stmt = select([census])

stmt = stmt.where(
    and_(census.columns.state == 'New York',
        or_(census.columns.state == 21,
            census.columns.age == 37)
    )
)

for result in connection.execute(stmt):
    print(result.age, result.state, result.sex)