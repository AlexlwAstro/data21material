import sqlalchemy
import pandas as pd

server = 'localhost,1433'
database = 'Northwind'
user = 'SA'
password = 'Passw0rd2018'
driver = 'SQL+Server'
# ODBC+Driver+17+for+
engine = sqlalchemy.create_engine(f"mssql+pyodbc://{user}:{password}@{server}/{database}?driver={driver}")

connection = engine.connect()

result = engine.execute('SELECT * FROM Products P INNER JOIN [Order Details] OD ON OD.ProductID = P.ProductID;')
print(result)

#first_row = result.fetchone()
#print(first_row)

#print('next query')
all_rows = result.fetchall()
#list_all_rows = list(all_rows)
#print(list_all_rows)

print(list(result.keys()))
#for entry in result:
#    entry_dict = dict(entry)
#    print(entry_dict.keys())
