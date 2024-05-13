import pyodbc
from datetime import datetime
from typing import List


server_name = "DESKTOP-0EUUQEO\\SQLEXPRESS"
database_name = "SISDB"

conn_str = (
    f"Driver={{SQL Server}};"
    f"Server={server_name};"
    f"Database={database_name};"
    f"Trusted_Connection=yes;"
)

print("Welcome to the movies app")
print(conn_str)

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

def connect_to_database():
     """
     Connects to the SQL Server database.
     """
     conn = pyodbc.connect(conn_str)
     cursor = conn.cursor()
     return conn, cursor

def close_connection(conn, cursor):
     """
     Closes the database connection and cursor.
     """
     cursor.close()
     conn.close()

def get_students():
     """
     Retrieves all students from the Students table.
     """
     conn, cursor = connect_to_database()
     cursor.execute("SELECT * FROM Students")
     students = cursor.fetchall()
     # close_connection(conn, cursor)
     print(students)

def insert_student(student_id: int, first_name: str, last_name: str, date_of_birth: datetime, email: str, phone_number: str):
     """
     Inserts a new student into the Students table.
     """
     conn, cursor = connect_to_database()
     query = "INSERT INTO Students (student_id, first_name, last_name, date_of_birth, email, phone_number) VALUES (?, ?, ?, ?, ?, ?)"
     cursor.execute(query, (student_id, first_name, last_name, date_of_birth, email, phone_number))
     conn.commit()
     # close_connection(conn, cursor)

def get_courses():
     """
     Retrieves all courses from the Courses table.
     """
     conn, cursor = connect_to_database()
     cursor.execute("SELECT * FROM Courses")
     courses = cursor.fetchall()
     # close_connection(conn, cursor)
     return courses

def insert_course(course_id: int, course_name: str, course_code: str, instructor_name: str):
    """
    Inserts a new course into the Courses table.
    """
    conn, cursor = connect_to_database()
    query = "INSERT INTO Courses (course_id, course_name, course_code, instructor_name) VALUES (?, ?, ?, ?)"
    cursor.execute(query, (course_id, course_name, course_code, instructor_name))
    conn.commit()
#     # close_connection(conn, cursor)

def get_enrollments():
    """
    Retrieves all enrollments from the Enrollments table.
    """
    conn, cursor = connect_to_database()
    cursor.execute("SELECT * FROM Enrollments")
    enrollments = cursor.fetchall()
    # close_connection(conn, cursor)
    return enrollments

def insert_enrollment(enrollment_id: int, student_id: int, course_id: int, enrollment_date: datetime):
    """
    Inserts a new enrollment into the Enrollments table.
    """
    conn, cursor = connect_to_database()
    query = "INSERT INTO Enrollments (enrollment_id, student_id, course_id, enrollment_date) VALUES (?, ?, ?, ?)"
    cursor.execute(query, (enrollment_id, student_id, course_id, enrollment_date))
    conn.commit()
#     # close_connection(conn, cursor)

def get_teachers():
    """
    Retrieves all teachers from the Teachers table.
    """
    conn, cursor = connect_to_database()
    cursor.execute("SELECT * FROM Teachers")
    teachers = cursor.fetchall()
    # close_connection(conn, cursor)
    return teachers

def insert_teacher(teacher_id: int, first_name: str, last_name: str, email: str):
    """
    Inserts a new teacher into the Teachers table.
    """
    conn, cursor = connect_to_database()
    query = "INSERT INTO Teachers (teacher_id, first_name, last_name, email) VALUES (?, ?, ?, ?)"
    cursor.execute(query, (teacher_id, first_name, last_name, email))
    conn.commit()
    # close_connection(conn, cursor)

def get_payments():
    """
#     Retrieves all payments from the Payments table.
#     """
    conn, cursor = connect_to_database()
    cursor.execute("SELECT * FROM Payments")
    payments = cursor.fetchall()
    # close_connection(conn, cursor)
    return payments

def insert_payment(payment_id: int, student_id: int, amount: float, payment_date: datetime):
#     """
#     Inserts a new payment into the Payments table.
#     """
    conn, cursor = connect_to_database()
    query = "INSERT INTO Payments (payment_id, student_id, amount, payment_date) VALUES (?, ?, ?, ?)"
    cursor.execute(query, (payment_id, student_id, amount, payment_date))
    conn.commit()
    # close_connection(conn, cursor)