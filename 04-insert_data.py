import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from datetime import datetime

try:
    # Create a connection with the database
    conn = mysql.connector.connect(host='localhost', database='students',
                                   user='studentadmin', password='password')

  # 3. Insert multiple rows with one query
    query = """INSERT INTO classes VALUES
    ('English', NULL), ('Speech', NULL), ('Literature', NULL),
    ('Algebra', NULL), ('Geometry', NULL), ('Trigonometry', NULL),
    ('Calculus', NULL), ('Earth Science', NULL), ('Biology', NULL),
    ('Chemistry', NULL), ('Physics', NULL), ('History', NULL), ('Art', NULL),
    ('Gym', NULL)"""

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
