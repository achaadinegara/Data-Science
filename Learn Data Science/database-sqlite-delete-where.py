import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sqlalchemy import MetaData, Table, create_engine, select, func, and_

metadata = MetaData()

engine = create_engine('mysql+pymysql://student:datacamp@courses.csrrinzqubik.us-east-1.rds.amazonaws.com:3306/census')
connection = engine.connect()
census = Table('census', metadata, autoload=True, autoload_with=engine)

engine1 = create_engine('sqlite:///employees.sqlite')
print(engine1.table_names())

connection = engine1.connect()
employees = Table('employees', metadata, autoload=True, autoload_with=engine1)
extra_employees = Table('extra_employees', metadata, autoload=True, autoload_with=engine1)

print(extra_employees.columns.keys())

from sqlalchemy import delete

stmt = select([
    func.count(extra_employees.columns.name)
])

connection.execute(stmt).scalar()
delete_stmt = delete (extra_employees)
result_proxy = connection.execute(delete_stmt)
print(result_proxy.rowcount)

stmt = delete(employees).where(employees.columns.id == 3)

result_proxy_satu = connection.execute(stmt)
print(result_proxy_satu.rowcount)