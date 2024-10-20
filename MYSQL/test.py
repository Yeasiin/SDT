import mysql.connector

database_name  = 'python'

db = mysql.connector.connect(
    host = "localhost",
    user="root",
    password="root",
    database=database_name
)

cursor = db.cursor();



query = f"CREATE DATABASE {database_name}"

cursor.execute(query)







