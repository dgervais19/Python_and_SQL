### Task
- Create a new file and a class with function to establish connection with pyodbc
- Create a function that create a table in the DB
- Create a function that prompts user to input data in that table
- Create a new file called PYODBC_TASK.md 

### Steps

1. Create a new .py file and import pyodbc
```
import pyodbc
```
2. Create a class that holds various methods to manipulate the Northwind database
```
class NW_Database:
```
3. Create a method that initialises the class and connects to database
```
    def __init__(self):
        self.server = "databases1.spartaglobal.academy"
        self.database = "Northwind"
        self.username = "**"
        self.password = "******"
        # establish connection
        self.northwind_connection = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)

        self.cursor = self.northwind_connection.cursor()
```
4. Create a method that creates a table in the database
```
 def create_table(self):
        self.cursor.execute("""CREATE TABLE Dono_Keys (Name VARCHAR(255), Keyboard_Brand VARCHAR(255), Keyboard_Model VARCHAR(255)); """)

        Dono_table = self.cursor.execute("SELECT * FROM Dono_keys;").fetchall()
        return (Dono_table)
```
5. Create a method that allows user input to insert data into the table
```
    def user_insert(self,):
        name = str(input("Enter your first name or musician name ==> "))
        keyboard_brand = str(input("Enter a keyboard brand ==> "))
        keyboard_model = (input("Enter a model for that brand ==> "))
        self.cursor.execute(f"INSERT INTO Dono_Keys (Name, Keyboard_Brand, Keyboard_Model) VALUES ('{name}', '{keyboard_brand}', '{keyboard_model}');")

        self.northwind_connection.commit()
        self.Dono_table = self.cursor.execute("SELECT * FROM Dono_Keys;")
        return self.Dono_table
```
6. Create a method that allows you to view the data in the table
```
 def view_table(self):
        self.Dono_table = self.cursor.execute("SELECT * FROM Dono_Keys;").fetchall()
        for item in self.Dono_table:
            print(item)
```
7. Finally, create an object for your class in order to test it's methods
```
if __name__ == '__main__':
    test = NW_Database()
    test.__init__()
    test.create_table()
    test.user_insert()
    test.view_table()
```