import mysql.connector


db = mysql.connector.connect(
    host = "localhost",
    user="root",
    password="root",
    
)

database_name  = 'python'
cursor = db.cursor();


query = f"CREATE DATABASE {database_name}"

cursor.execute(query)







