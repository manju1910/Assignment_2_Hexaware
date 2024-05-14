import pyodbc
from typing import List
from DAO.course_service import CourseService
from DAO.enrollment_service import EnrollmentService
from DAO.payment_service import PaymentService
from DAO.student_service import StudentService
from DAO.teacher_service import TeacherService
server_name= "DESKTOP-0EUUQEO\\SQLEXPRESS"
database_name = "SISDB"
 
 
conn_str = (
    f"Driver={{SQL Server}};"
    f"Server={server_name};"
    f"Database={database_name};"
    f"Trusted_Connection=yes;"
)
 
 
print(conn_str)
conn = pyodbc.connect(conn_str)










          


