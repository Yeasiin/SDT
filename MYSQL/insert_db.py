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
    INSERT INTO Student(name) VALUES("REZAUL")
"""


cursor.execute(query)
db.commit()







