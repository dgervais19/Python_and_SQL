from nw_products import NW_Products

import pyodbc

class NW_runner(NW_Products):
    def __init__(self):
        super().__init__()
        self.stock = self.cursor.execute("SELECT UnitsInStock FROM Products;")

    def avg_UnitStock(self):
        stockID = []
        for num in self.stock:
            stockID.append(num[0])
        return sum(stockID)/len(stockID)



if __name__ == '__main__':
    test = NW_runner()
    print(test.avg_UnitStock())