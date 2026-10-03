import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2003")

if conn.is_connected():
    print("Successfully connected to the database")
print(conn)    
print(conn.is_connected())