from SQL_Task import Database

import pyodbc

class Average(Database):
    def __init__(self):
        super().__init__()
        self.products = self.cursor.execute("SELECT * FROM Products;")

    def avg_UnitStock(self):
        unit_in_stock = self.cursor.execute("SELECT UnitsInStock FROM Products;")
