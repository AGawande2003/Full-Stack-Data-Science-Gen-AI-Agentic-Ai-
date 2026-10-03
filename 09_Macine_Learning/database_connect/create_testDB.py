import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2003")

if conn.is_connected():
    print("Successfully connected to the database")
print(conn)    
print(conn.is_connected())


mycusor = conn.cursor()
mycusor.execute("show databases")
for db in mycusor:
    print(db)

mycusor.execute("Create database if not exists Python_db")
print("Database created successfully")
print(mycusor)