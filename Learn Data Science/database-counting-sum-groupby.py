from sqlalchemy import MetaData, Table, create_engine, select, desc, func

metadata = MetaData()

engine = create_engine('sqlite:///census.sqlite')

connection = engine.connect()

census = Table('census', metadata, autoload=True, autoload_with=engine)

stmt = select([census.columns.sex,
        func.sum(census.columns.pop2008)])

stmt = stmt.group_by(census.columns.sex)

results = connection.execute(stmt).fetchall()
print(results)