import mysql.connector

# 1. Establish the database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2003",
    database="python_db"
)

if conn.is_connected():
    print("Successfully connected to the database")

mycursor = conn.cursor()

# 2. Corrected CREATE TABLE statement (added closing parenthesis)
create_table_query = """
CREATE TABLE IF NOT EXISTS student (
    name VARCHAR(255),
    branch VARCHAR(255),
    id INT
)
"""
mycursor.execute(create_table_query)
print("Table created or already exists.")

# 3. Insert multiple records using parameterized values
sql = "INSERT INTO student (name, branch, id) VALUES (%s, %s, %s)"
val = [
    ("adarsh", "cse", 56),
    ("rohit", "eee", 57),
    ("ram", "mech", 58)
]

mycursor.executemany(sql, val)

# 4. Commit transaction to persist changes in MySQL
conn.commit()
print(mycursor.rowcount, "records inserted successfully.")

# 5. Clean up cursor and connection resources
mycursor.close()
conn.close()