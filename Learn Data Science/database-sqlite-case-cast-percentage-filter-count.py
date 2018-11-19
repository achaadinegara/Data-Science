from sqlalchemy import create_engine, MetaData, Table, select, func, desc, case, cast, Float

metadata = MetaData()

engine = create_engine('mysql+pymysql://student:datacamp@courses.csrrinzqubik.us-east-1.rds.amazonaws.com:3306/census')

connection = engine.connect()

census = Table('census', metadata, autoload=True, autoload_with = engine)

female_pop2000 = func.sum(
    case([
        (census.columns.sex == 'F', census.columns.pop2000)
    ], else_=0)
)

total_pop2000 = cast(func.sum(census.columns.pop2000), Float)
stmt = select([female_pop2000 / total_pop2000 * 100])
percent_female = connection.execute(stmt).scalar()

print(percent_female)