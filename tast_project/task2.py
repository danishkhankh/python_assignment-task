########################################################################
# Task 3: MySQL Database Operations with Python
########################################################################


import mysql.connector

def connect_to_database():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        port='3306',
        database='student'
    )
    cursor = connection.cursor()
    return connection, cursor

########################################################################
#create
########################################################################
def create_students_table(cursor):
    cursor.execute("""
        CREATE TABLE  students (
            student_id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            age INT,
            grade FLOAT
        )
    """)

########################################################################
#insert data
########################################################################
def insert(cursor, first_name, last_name, age, grade):
    cursor.execute("""
        INSERT INTO students (first_name, last_name, age, grade)
        VALUES (%s, %s, %s, %s)
    """, (first_name, last_name, age, grade))

########################################################################
#update data
########################################################################
def update(cursor, first_name, new_grade):
    cursor.execute("""
        UPDATE students
        SET grade = %s
        WHERE first_name = %s
    """, (new_grade, first_name))

########################################################################
# delete data
########################################################################
def delete(cursor, last_name):
    cursor.execute("""
        DELETE FROM students
        WHERE last_name = %s
    """, (last_name,))

# Function to fetch and display all student records
def fetch(cursor):
    cursor.execute("""
        SELECT * FROM students
    """)
    students = cursor.fetchall()

    print("Student Records:")
    for student in students:
        print(student)

######################################################
# Connect to the database

connection, cursor = connect_to_database()
################################################################


###############################################################################
# Insert a new student
insert(cursor, "Alice", "Smith", 18, 95.5)
################################################################################

# Update the grade and  name
update(cursor, "Alice", 97.0)
################################################################################


# Delete "Smith"
delete(cursor, "Smith")
################################################################################

# Fetch and display all student records
fetch(cursor)
################################################################################

# Commit changes and close the connection
connection.commit()
connection.close()




# note  call insert() function commit other function
# note  call update() function commit other function
# note  call delete() function commit other function
# note  call fetch() function commit other function