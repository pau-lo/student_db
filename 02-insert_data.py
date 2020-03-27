import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from datetime import datetime

try:
    # Create a connection with the database
    conn = mysql.connector.connect(host='localhost',
                                   database='students', user='studentadmin',
                                   password='password')

    # Query used to insert data
    query = """INSERT INTO students VALUES
    (NULL, 'Dale', 'Cooper', '1959-2-22', 'dcooper@aol.com',
     '123 Main St', 'Yakima', 'WA', 98901, '792-223-8901', 'M',
     NOW(), 'math 101', 'A', 3.50)"""

    cursor = conn.cursor()
    # Insert multiple rows with one query
    cursor.execute(query)

    # Send the transaction to MySQL
    conn.commit()
    print("Data Entered")
    # Reset results and close the cursor
    cursor.close()

# Catch any errors
except mysql.connector.Error as error:
    print("Error :", error)

# Always executes and makes sure the DB connection is
# released
finally:
    if(conn.is_connected()):
        conn.close()
        print("Database Connection Closed")
