# import all the correct packages to connect with SQL
import pyodbc
import csv

# create class for the DB with the methods that will manipulate the DB
class CRUD_DB:
    def __init__(self):
        self.connection()

    def connection(self):
        self.server = "databases1.spartaglobal.academy"
        self.database = "Northwind"
        self.username = "SA"
        self.password = "Passw0rd2018"
        # establish connection
        self.northwind_connection = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)

        self.cursor = self.northwind_connection.cursor()


    def read_csv(self):
        with open('imdbtitles.csv', "r") as csvfile:
            self.reader = csv.reader(csvfile)
            self.data_list = []
            for row in self.reader:
                self.data_list.append(row)
            return self.data_list

    # def create_table(self):
    #     column_name = []
    #     column_name = self.data_list





test = CRUD_DB()
test.read_csv()
