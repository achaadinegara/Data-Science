from sqlalchemy import create_engine, MetaData, Table, select, func, desc

metadata = MetaData()

engine = create_engine('mysql+pymysql://student:datacamp@courses.csrrinzqubik.us-east-1.rds.amazonaws.com:3306/census')

connection = engine.connect()

census = Table('census', metadata, autoload=True, autoload_with=engine)

stmt = select([census.columns.state, (census.columns.pop2008-census.columns.pop2000).label('pop_change')])

stmt =  stmt.group_by(census.columns.state)

stmt = stmt.order_by(desc('pop_change'))

stmt = stmt.limit(5)

results = connection.execute(stmt).fetchall()

for result in results:
    print('{}:{}'.format(result.state, result.pop_change))