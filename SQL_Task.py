import pyodbc

class Database:

    def db_connect(self):
        server = "databases1.spartaglobal.academy"
        database = "Northwind"
        username = "SA"
        password = "Passw0rd2018"
        northwind_connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL   Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

    def create_table(self):
