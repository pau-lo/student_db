import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from datetime import datetime

try:
    # Create a connection with the database
    conn = mysql.connector.connect(host='localhost',
                                   database='students', user='studentadmin',
                                   password='password')

    # Insert absences
    query = """INSERT INTO absences VALUES 
    (6, '2014-08-29'),(7, '2014-08-29'),(8, '2014-08-27')"""

    # The cursor object provides methods we can use to
    # interact with the database
    cursor = conn.cursor()
    # Execute the query
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
