import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from datetime import datetime

try:
    # Create a connection with the database
    conn = mysql.connector.connect(host='localhost',
                                   database='students', user='studentadmin',
                                   password='password')

    query = """INSERT INTO scores VALUES 
    (1, 1, 15),(1, 2, 14),(1, 3, 28),(1, 4, 29),(1, 5, 15),(1, 6, 27),
    (2, 1, 15),(2, 2, 14),(2, 3, 26),(2, 4, 28),(2, 5, 14),(2, 6, 26),
    (3, 1, 14),(3, 2, 14),(3, 3, 26),(3, 4, 26),(3, 5, 13),(3, 6, 26),
    (4, 1, 15),(4, 2, 14),(4, 3, 27),(4, 4, 27),(4, 5, 15),(4, 6, 27),
    (5, 1, 14),(5, 2, 13),(5, 3, 26),(5, 4, 27),(5, 5, 13),(5, 6, 27),
    (6, 1, 13),(6, 2, 13),(6, 4, 26),(6, 5, 13),(6, 6, 26),(7, 1, 13),
    (7, 2, 13),(7, 3, 25),(7, 4, 27),(7, 5, 13),(8, 1, 14),(8, 3, 26),
    (8, 4, 23),(8, 5, 12),(8, 6, 24),(9, 1, 15),(9, 2, 13),(9, 3, 28),
    (9, 4, 27),(9, 5, 14),(9, 6, 27),(10, 1, 15),(10, 2, 13),
    (10, 3, 26),(10, 4, 27),(10, 5, 12), (10, 6, 22)"""

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
