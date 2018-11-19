from sqlalchemy import MetaData, Table, create_engine, select, desc, func

metadata = MetaData()

engine = create_engine('sqlite:///census.sqlite')

connection = engine.connect()

census = Table('census', metadata, autoload=True, autoload_with=engine)

stmt = select([func.sum(census.columns.pop2008)])

results = connection.execute(stmt).scalar()

print(results)