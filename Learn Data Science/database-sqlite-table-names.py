from sqlalchemy import create_engine

engine = create_engine('sqlite:///census.sqlite')

print(engine.table_names())