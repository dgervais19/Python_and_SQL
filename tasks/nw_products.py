from SQL_Task import NW_Database
import pyodbc

class NW_Products(NW_Database):
    def __init__(self):
        super().__init__()
        self.products = self.cursor.execute("SELECT * FROM Products;")