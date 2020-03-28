import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(host='localhost', database='students',
                                   user='studentadmin', password='password')

    query = """SELECT state, COUNT(state) AS "Amount"
            FROM students GROUP BY state HAVING amount > 1"""

    cursor = conn.cursor()
    cursor.execute(query)
    students = cursor.fetchall()
    print("Total Results :", len(students))
    for s in students:
        print(s[0], "", s[1])
except mysql.connector.Error as error:
    print("Error :", error)
finally:
    if(conn.is_connected()):
        conn.close()
