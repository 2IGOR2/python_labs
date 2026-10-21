#Задание 3


import sqlite3

con = sqlite3.connect("database.db")

cursor = con.cursor()

cursor.execute("""CREATE TABLE Students(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER)
                CREATE TABLE Teachers(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER)""")


# cursor.execute("SELECT name FROM sqlite_master where type = 'table';")

# tables = cursor.fetchall()
# for table in tables:
#     print(table)
#     print(table[0])

con.close()