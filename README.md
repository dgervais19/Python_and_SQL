# Python with SQL
## Using PYODBC (open database connectivity) to connect SQL to our Python program
### What is a Cursor and how to use it
**some functions that we can use to interact with SQL data**

- Set up the pyodbc connection
- Command to install pyodbc
```pip install pyodbc```
- once installed create a python_sql.py file


**Establish a Connection**
```
# This lesson will include connection to our SQL DB from Python using PYODBC

import pyodbc

import requests

# pyodbc driver from microsoft helps us to connect to SQL instance
# we will connect our Northwind DB which you have already used in SQL week

server = "databases1.spartaglobal.academy"
database = "Northwind"
username = "**"
password = "************"
northwind_connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

# server name - database name - username and password is required to connect to pyodbc
```


* Run a Query to search for the data in our Customers table



**Summary**
- pyodbc installation and connection set up 
- cursor utilisation
- fetchone() (select and record)
- fetchall() (select all records)

### Task
- Create a new file and a class with function to establish connection with pyodbc
- Create a function that create a table in the DB
- Create a function that prompts user to input data in that table
- Create a new file called PYODBC_TASK.md 