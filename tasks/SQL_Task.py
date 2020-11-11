# import pyodbc
import pyodbc

# Create a class for the database
class NW_Database:
# initialise the class
    def __init__(self):
        self.server = "databases1.spartaglobal.academy"
        self.database = "Northwind"
        self.username = "**"
        self.password = "******"
        # establish connection
        self.northwind_connection = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)

        self.cursor = self.northwind_connection.cursor()

    def create_table(self):
        self.cursor.execute("""CREATE TABLE Dono_Keys (Name VARCHAR(255), Keyboard_Brand VARCHAR(255), Keyboard_Model VARCHAR(255)); """)

        Dono_table = self.cursor.execute("SELECT * FROM Dono_keys;").fetchall()
        return (Dono_table)

    def user_insert(self,):
        name = str(input("Enter your first name or musician name ==> "))
        keyboard_brand = str(input("Enter a keyboard brand ==> "))
        keyboard_model = (input("Enter a model for that brand ==> "))
        self.cursor.execute(f"INSERT INTO Dono_Keys (Name, Keyboard_Brand, Keyboard_Model) VALUES ('{name}', '{keyboard_brand}', '{keyboard_model}');")

        self.northwind_connection.commit()
        self.Dono_table = self.cursor.execute("SELECT * FROM Dono_Keys;")
        return self.Dono_table

    def view_table(self):
        self.Dono_table = self.cursor.execute("SELECT * FROM Dono_Keys;").fetchall()
        for item in self.Dono_table:
            print(item)


# Carry out various test to check the code
if __name__ == '__main__':
    test = NW_Database()
    test.__init__()
    test.create_table()
    test.user_insert()
    test.view_table()
