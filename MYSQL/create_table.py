import mysql.connector

database_name  = 'python'

db = mysql.connector.connect(
    host = "localhost",
    user="root",
    password="root",
    database=database_name
)

cursor = db.cursor();

query = """CREATE TABLE Student(
    roll INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50)
)"""



cursor.execute(query)







