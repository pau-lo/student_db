import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from datetime import datetime

try:
    # Create a connection with the database
    conn = mysql.connector.connect(host='localhost',
                                   database='students', user='studentadmin',
                                   password='password')

    # 2. Create a parameterized query
    query = """INSERT INTO students
    (student_id, first_name, last_name, birth_date, email, street, city, state,
     zip, phone, gender, date_entered, course, grade, lunch_cost) VALUES
    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    # 2. Get the current time and format it to fit what
    # MySQL expects
    now_time = datetime.now()
    format_date = now_time.strftime('%Y-%m-%d %H:%M:%S')

    # 2. Insert multiple rows
    # You must use None instead of NULL
    students = [(None, 'Harry', 'Truman', '1946-1-24', 'htruman@aol.com', '202 South St',
                 'Vancouver', 'WA', 98660, '792-223-9810', 'M', format_date, 'math 101', 'C',  3.50),
                (None, 'Shelly', 'Johnson', '1970-12-12', 'sjohnson@aol.com', '9 Pond Rd',
                 'Sparks', 'NV', 89431, '792-223-6734', 'F', format_date, 'math 101', 'A', 3.50),
                (None, 'Bobby', 'Briggs', '1967-5-24', 'bbriggs@aol.com', '14 12th St',
                 'San Diego', 'CA', 92101, '792-223-6178', 'M', format_date, 'math 101', 'B', 3.50),
                (None, 'Donna', 'Hayward', '1970-3-24', 'dhayward@aol.com', '120 16th St',
                 'Davenport', 'IA', 52801, '792-223-2001', 'F', format_date, 'math 101', 'A', 3.50),
                (None, 'Audrey', 'Horne', '1965-2-1', 'ahorne@aol.com', '342 19th St', 'Detroit',
                 'MI', 48222, '792-223-2001', 'F', format_date, 'math 101', 'A', 3.50),
                (None, 'James', 'Hurley', '1967-1-2', 'jhurley@aol.com', '2578 Cliff St',
                 'Queens', 'NY', 11427, '792-223-1890', 'M', format_date, 'math 101', 'A', 3.50),
                (None, 'James', 'Hurley', '1967-1-7', 'jhurley@aol.com', '2578 Cliff St',
                 'Queens', 'NY', 11427, '792-223-1890', 'M', format_date, 'math 101', 'A', 3.50),
                (None, 'Lucy', 'Moran', '1951-12-3', 'lmoran@aol.com', '178 Dover St', 'Hollywood',
                 'CA', 90078, '792-223-9678', 'F', format_date, 'math 101', 'B', 3.50),
                (None, 'Tommy', 'Hill', '1977-11-4', 'thill@aol.com', '672 High Plains',
                 'Tucson', 'AZ', 85701, '792-223-1115', 'M', format_date, 'math 101', 'A', 3.50),
                (None, 'Andy', 'Brennan', '1960-12-27', 'abrennan@aol.com', '281 4th St',
                 'Jacksonville', 'NC', 28540, '792-223-8902', 'M', format_date, 'math 101', 'A', 3.50)
                ]

    # The cursor object provides methods we can use to
    # interact with the database
    cursor = conn.cursor()
    # Execute the query
    # Insert multiple rows of data from the list
    cursor.executemany(query, students)

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
