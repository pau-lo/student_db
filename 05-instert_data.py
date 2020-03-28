import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from datetime import datetime

try:
    # Create a connection with the database
    conn = mysql.connector.connect(host='localhost', database='students',
                                   user='studentadmin', password='password')

    query = """INSERT INTO tests VALUES ('2014-8-25', 'Q', 15, 1, NULL),
    ('2014-8-27', 'Q', 15, 1, NULL), ('2014-8-29', 'T', 30, 1, NULL),
    ('2014-8-29', 'T', 30, 2, NULL), ('2014-8-27', 'Q', 15, 4, NULL),
    ('2014-8-29', 'T', 30, 4, NULL)"""

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
