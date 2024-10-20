import mysql.connector

database_name  = 'python'

db = mysql.connector.connect(
    host = "localhost",
    user="root",
    password="root",
    database=database_name
)

cursor = db.cursor();



query = """
    UPDATE Student
    SET name = "Rezaul Korim"
    WHERE roll = 7
    
"""


cursor.execute(query)
db.commit()







