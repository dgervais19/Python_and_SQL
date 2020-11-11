import pyodbc

class Database:
# initialise the class
    def __init__(self):
        self.server = "databases1.spartaglobal.academy"
        self.database = "Northwind"
        self.username = "SA"
        self.password = "Passw0rd2018"
        # establish
        self.northwind_connection = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        self.cursor = self.northwind_connection.cursor()

    def create_table(self):
        self.cursor.execute("CREATE TABLE Dono_keys (Name VARCHAR(100), Brand VARCHAR(100), Model VARCHAR(100);")
        Dono_table = self.cursor.execute("SELECT * FROM Dono_keys;").fetchall()
        return (Dono_table)
        # self.cursor.execute("SELECT @@VERSION")
        # row = self.cursor.fetchone()
        # print(row)
    def user_insert(self):
        keyboard_brand = input("Enter a keyboard brand ==> ")
        keyboard_model = input("Enter a model for that brand ==> ")
        self.cursor.execute(f"INSERT INTO Dono_keys (Brand, Model) VALUES ({keyboard_brand}, {keyboard_model});")

    def view_table(self):
        for item in self.Dono_table:
            print(item)


test = Database()
test.__init__()
test.create_table()
# test.user_insert("Roland", "RD800")
# print(test.view_table())
