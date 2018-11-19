from sqlalchemy import MetaData, Table, create_engine, select

metadata = MetaData()

engine = create_engine('sqlite:///census.sqlite')

connection = engine.connect()

census = Table('census', metadata, autoload=True, autoload_with = engine)

print(repr(census))