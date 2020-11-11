
# This lesson will include connection to our SQL DB from Python using PYODBC

import pyodbc

import requests

# pyodbc driver from microsoft helps us to connect to SQL instance
# we will connect our Northwind DB which you have already used in SQL week

server = "databases1.spartaglobal.academy"
database = "Northwind"
username = "**"
password = "*******"
northwind_connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

# server name - database name - username and password is required to connect to pyodbc
cursor = northwind_connection.cursor()
# cursor is the location of your mouse/current path

cursor.execute("SELECT @@VERSION")
# select the version of current DB
row = cursor.fetchone()
print(row)

# In our DB we have table called Customers that has customers data available
cust_row = cursor.execute("SELECT * FROM Customers;").fetchall()
print(type(cust_row))
for records in cust_row:
    print(records)

# We have another table in the DB called products

product_rows = cursor.execute("SELECT * FROM Products").fetchall()
# Running queries in our python program to access database and table inside the DBs
for product_records in product_rows:
# iterate through the table data and find the unit prices
    print(product_records.UnitPrice)
print(product_rows)

product_row = cursor.execute("SELECT * FROM Products;")
# getting the Product table

# Iterating through the data until the last line of the data (until condition is false)

# Combination of our loop and control flow to ensure we only iterate through the data as long as the data is available
while True:
    records = product_row.fetchone()
    if records is None:
        # when there is no records left (value is None) stop
        break
    print(records.UnitPrice)