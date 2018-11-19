from sqlalchemy import MetaData, Table, create_engine, select, and_, or_

metadata = MetaData()

engine = create_engine('sqlite:///census.sqlite')

connection = engine.connect()

census = Table('census', metadata, autoload=True, autoload_with=engine)

stmt = select([census])

stmt = stmt.where(
    and_(census.columns.state == 'California',
        census.columns.sex != 'M')
)

for result in connection.execute(stmt):
    print(result.age, result.sex)

