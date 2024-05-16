
from util.dbconnection import Dbconnection
from dao.services import *
from Exception.myexceptions import DuplicateEnrollmentException,CourseNotFoundException,StudentNotFoundException,TeacherNotFoundException,PaymentValidationException,InvalidStudentDataException,InvalidCourseDataException,InvalidEnrollmentDataException,InvalidTeacherDataException,InsufficientFundsException
# from Entity import Course, Enrollment, Teacher, Payment,Student


class StudentServiceImpl(StudentDAO):
    def __init__(self):
        server_name = "DESKTOP-0EUUQEO\\SQLEXPRESS"
        database_name = "SISDB"
        conn_str = (
            f"Driver={{SQL Server}};"
            f"Server={server_name};"
            f"Database={database_name};"
            f"Trusted_Connection=yes;"
        )
    def add_student(self):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
        email = input("Enter email: ")
        phone_number = input("Enter phone number: ")
        if not first_name or not last_name or not date_of_birth or not email or not phone_number:
            raise InvalidStudentDataException("All fields are required.")
        date_of_birth = str(date_of_birth)
        phone_number = str(phone_number)

        stmt = self.conn.cursor()
        stmt = self.conn.cursor()
        stmt.execute(
            "INSERT INTO students (first_name, last_name, date_of_birth, email, phone_number) VALUES (%s, %s, %s, %s, %s)",
            (first_name, last_name, date_of_birth, email, phone_number))
        self.conn.commit()
        print("student added successfully!")

    def update_student(self):
        student_id = input("Enter the student ID to update: ")
        first_name = input("Enter updated first name: ")
        last_name = input("Enter updated last name: ")
        date_of_birth = input("Enter updated date of birth (YYYY-MM-DD): ")
        email = input("Enter updated email: ")
        phone_number = input("Enter updated phone number: ")
        date_of_birth = str(date_of_birth)
        phone_number = str(phone_number)
        stmt = self.conn.cursor()
        stmt.execute(
            "UPDATE students SET first_name=%s, last_name=%s, date_of_birth=%s, email=%s, phone_number=%s WHERE student_id=%s",
            (first_name, last_name, date_of_birth, email, phone_number, student_id))
        self.conn.commit()
        print("student updated successfully!")

    def get_student(self):
        try:
            student_id = int(input("Enter student_id: "))
            print("Searching for student with ID:", student_id)

            stmt = self.conn.cursor()
            stmt.execute("SELECT * FROM students WHERE student_id = %s", (student_id,))
            print("SQL query executed successfully")

            row = stmt.fetchone()
            if row:
                print("Student found:", row)
                student = Student(*row)
                return student
            else:
                raise StudentNotFoundException(f"No student found with ID: {student_id}")

        except StudentNotFoundException as e:
            raise e
        except Exception as e:
            print("Error retrieving student:", e)
            return None

    def delete_student(self):
        student_id=int(input("Enter student_id :"))
        stmt = self.conn.cursor()
        stmt.execute("DELETE FROM students WHERE student_id= %s ", (student_id,))
        self.conn.commit()
        print("student deleted successfully!")

    def get_all_students(self):
        try:
            stmt = self.conn.cursor()
            stmt.execute("SELECT * FROM students")
            students = [Student(*row) for row in stmt.fetchall()]
            if students:
                print("All students:")
                for student in students:
                    print(f"Student ID: {student.student_id}")
                    print(f"First Name: {student.first_name}")
                    print(f"Last Name: {student.last_name}")
                    print(f"Date of Birth: {student.date_of_birth}")
                    print(f"Email: {student.email}")
                    print(f"Phone Number: {student.phone_number}")
                    print()
                print("All students retrieved successfully")
            else:
                print("No students found.")
        except Exception as e:
            print("Error retrieving students:", str(e))


class CourseServiceImpl(CourseDAO):
    def __init__(self):
        server_name = "DESKTOP-0EUUQEO\\SQLEXPRESS"
        database_name = "SISDB"
        conn_str = (
            f"Driver={{SQL Server}};"
            f"Server={server_name};"
            f"Database={database_name};"
            f"Trusted_Connection=yes;"
        )

    def add_course(self):
        course_id=int(input("Enter course_id :"))
        course_name=input("Enter course name :")
        teacher_id=int(input("Enter teacher_id :"))
        credits = int(input("Enter credits :"))
        if not course_name or credits <= 0:
            raise InvalidCourseDataException("Course name is required and credits should be a positive number.")
        stmt = self.conn.cursor()
        stmt.execute("INSERT INTO courses VALUES (%s, %s, %s, %s)",
                            (course_id,course_name,teacher_id,credits))
        self.conn.commit()
        print("course added successfully!")


    def update_course(self):
        course_name = input("Enter course name :")
        teacher_id = int(input("Enter teacher_id :"))
        credits = int(input("Enter credits :"))
        course_id = int(input("Enter course_id :"))
        stmt = self.conn.cursor()
        stmt.execute("UPDATE courses SET course_name=%s, teacher_id=%s, credits=%s WHERE course_id=%s",
                     (course_name,teacher_id,credits,course_id))
        self.conn.commit()
        print("course updated successfully!")

    def get_course(self):
        try:
            course_id = int(input("Enter course_id: "))
            print("Searching for course with ID:", course_id)

            stmt = self.conn.cursor()
            stmt.execute("SELECT * FROM courses WHERE course_id = %s", (course_id,))
            print("SQL query executed successfully")

            row = stmt.fetchone()
            if row:
                course_id, course_name, credits,teacher_id =row
                print(f"Course ID: {course_id}")
                print(f"Course Name: {course_name}")
                print(f"credits: {credits}")
                print(f"teacher_id: {teacher_id}")
                print("course details retrieved successfully!")
            else:
                raise CourseNotFoundException(f"No course found with ID: {course_id}")

        except CourseNotFoundException as e:
            raise e

        except Exception as e:
            print("Error retrieving course:", e)
            return None



    def delete_course(self):
        course_id=int(input("Enter course_id :"))
        stmt = self.conn.cursor()
        stmt.execute("DELETE FROM courses WHERE course_id= %s", (course_id,))
        self.conn.commit()
        print("course deleted successfully!")

    def get_all_courses(self) -> List[Course]:
        try:
            stmt = self.conn.cursor()
            stmt.execute("SELECT * FROM courses")
            courses = [Course(*row) for row in stmt.fetchall()]
            if courses:
                print("All courses:")
                for course in courses:
                    print(f"Course ID: {course.course_id}")
                    print(f"Course name: {course.course_name}")
                    print(f"Credits: {course.credits}")
                    print(f"teacher ID: {course.teacher_id}")
                    print()
                print("All courses retrieved successfully!")
            else:
                print("No courses found.")
        except Exception as e:
            print("Error retrieving courses:", str(e))


class EnrollmentServiceImpl(EnrollmentDAO):
    def __init__(self):
        server_name = "DESKTOP-0EUUQEO\\SQLEXPRESS"
        database_name = "SISDB"
        conn_str = (
            f"Driver={{SQL Server}};"
            f"Server={server_name};"
            f"Database={database_name};"
            f"Trusted_Connection=yes;"
        )

    def add_enrollment(self):
        student_id=int(input("Enter student_id :"))
        course_id=int(input("Enter course_id :"))
        enrollment_date=input("Enter enrollment date :")
        if not enrollment_date:
            raise InvalidEnrollmentDataException("Enrollment date is required.")
        stmt = self.conn.cursor()
        stmt.execute("SELECT * FROM enrollments WHERE student_id = %s AND course_id = %s", (student_id, course_id))
        existing = stmt.fetchone()
        if existing:
            raise DuplicateEnrollmentException("Student is already enrolled in the course.")

        stmt.execute("INSERT INTO enrollments (student_id, course_id, enrollment_date) VALUES (%s, %s, %s)",
                     (student_id,course_id,enrollment_date))
        self.conn.commit()
        print("enrollment added successfully!")

    def update_enrollment(self):
        student_id=int(input("Enter student_id :"))
        course_id=int(input("Enter course_id :"))
        enrollment_date=input("Enter enrollment date :")
        enrollment_id=int(input("Enter enrollment id :"))
        stmt = self.conn.cursor()
        stmt.execute("UPDATE enrollments SET student_id= %s, course_id=%s, enrollment_date=%s WHERE enrollment_id=%s",
                            (student_id,course_id,enrollment_date,enrollment_id))
        self.conn.commit()
        print("enrollment updated successfully!")


    def get_enrollment(self):
        enrollment_id = int(input("Enter enrollment id :"))
        stmt = self.conn.cursor()
        stmt.execute("SELECT * FROM enrollments WHERE enrollment_id= %s", (enrollment_id,))
        row = stmt.fetchone()
        if row:
            enrollment_id,student_id,course_id,enrollment_date = row
            print(f"enrollment ID: {enrollment_id}")
            print(f"student ID: {student_id}")
            print(f"enrollment date: {enrollment_date}")
            print("enrollment details retrieved successfully!")
        else:
            print("No course found with ID:", enrollment_id)
            return None

    def delete_enrollment(self):
        enrollment_id=int(input("Enter Enrollment id :"))
        stmt = self.conn.cursor()
        stmt.execute("DELETE FROM enrollments WHERE enrollment_id= %s", (enrollment_id,))
        self.conn.commit()
        print("enrollment deleted successfully!")

    def get_all_enrollments(self) -> List[Enrollment]:
        try:
            stmt = self.conn.cursor()
            stmt.execute("SELECT * FROM enrollments")
            enrollments = [Enrollment(*row) for row in stmt.fetchall()]
            if enrollments:
                print("All enrollments:")
                for enrollment in enrollments:
                    print(f"enrollment ID: {enrollment.get_enrollment_id()}")
                    print(f"student ID: {enrollment.student_id}")
                    print(f"Course Id: {enrollment.course_id}")
                    print(f"enrollment_date: {enrollment.enrollment_date}")
                    print()
                print("All enrollments retrieved successfully!")
            else:
                print("No enrollments found.")
        except Exception as e:
            print("Error retrieving students:", str(e))


class TeacherServiceImpl(TeacherDAO):
    def __init__(self):
        server_name = "DESKTOP-0EUUQEO\\SQLEXPRESS"
        database_name = "SISDB"
        conn_str = (
            f"Driver={{SQL Server}};"
            f"Server={server_name};"
            f"Database={database_name};"
            f"Trusted_Connection=yes;"
        )

    def add_teacher(self):
        first_name=input("Enter first name :")
        last_name=input("Enter last name :")
        email=input("Enter email :")
        if not first_name or not last_name or not email:
            raise InvalidTeacherDataException("First name, last name, and email are required.")
        stmt = self.conn.cursor()
        stmt.execute("INSERT INTO teacher (first_name, last_name, email) VALUES (%s,%s, %s)",
                     (first_name,last_name,email))
        self.conn.commit()
        print("teacher added successfully!")

    def update_teacher(self):
        first_name=input("Enter first name :")
        last_name=input("Enter last name :")
        email = input("Enter email :")
        teacher_id=int(input("Enter teacher id :"))
        stmt = self.conn.cursor()
        stmt.execute("UPDATE teacher SET first_name= %s, last_name= %s, email= %s WHERE teacher_id= %s",
                            (first_name,last_name,email,teacher_id))
        self.conn.commit()
        print("teacher updated successfully!")


    def get_teacher(self):
        try:
            teacher_id=int(input("Enter teacher id :"))
            stmt = self.conn.cursor()
            stmt.execute("SELECT * FROM teacher WHERE teacher_id= %s", (teacher_id,))
            row = stmt.fetchone()
            if row:
                teacher_id,first_name,last_name,email = row
                print(f"teacher_id: {teacher_id}")
                print(f"first_name: {first_name}")
                print(f"last_name: {last_name}")
                print(f"email: {email}")
                print("teacher details retrieved successfully!")
            else:
                raise TeacherNotFoundException(f"No teacher found with ID: {teacher_id}")
        except TeacherNotFoundException as e:
            raise e

        except Exception as e:
            print("Error retrieving teacher:", e)
            return None

    def delete_teacher(self):
        teacher_id=int(input("Enter teacher id :"))
        stmt = self.conn.cursor()
        stmt.execute("DELETE FROM teacher WHERE teacher_id= %s", (teacher_id,))
        self.conn.commit()
        print("teacher deleted successfully!")

    def get_all_teachers(self) -> List[Teacher]:
        stmt = self.conn.cursor()
        stmt.execute("SELECT * FROM teacher")
        teachers = [Teacher(*row) for row in stmt.fetchall()]
        if teachers:
            print("All courses:")
            for teacher in teachers:
                print(f"teacher ID: {teacher.teacher_id}")
                print(f"first name: {teacher.first_name}")
                print(f"last name: {teacher.last_name}")
                print(f"email: {teacher.email}")
                print()
            print("All teachers retrieved successfully!")
        else:
            print("No teachers found.")
        return teachers


class PaymentServiceImpl(PaymentDAO):
    def __init__(self):
        server_name = "DESKTOP-0EUUQEO\\SQLEXPRESS"
        database_name = "SISDB"
        conn_str = (
            f"Driver={{SQL Server}};"
            f"Server={server_name};"
            f"Database={database_name};"
            f"Trusted_Connection=yes;"
        )

    def add_payment(self):
        payment_id=int(input("Enter payment id :"))
        student_id=int(input("Enter student id :"))
        amount=int(input("Enter amount :"))
        payment_date=input("Enter payment_date : ")
        if amount<0:
            raise InsufficientFundsException("Payment amount must be greater than 0.")
        if student_id <= 0:
            raise PaymentValidationException("Student ID must be positive")
        if amount <= 0:
            raise PaymentValidationException("Amount must be positive")
        stmt = self.conn.cursor()
        stmt.execute("INSERT INTO payments VALUES (%s, %s, %s, %s)",
                            (payment_id, student_id,amount,payment_date))
        self.conn.commit()
        print("payment added successfully!")

    def update_payment(self):
        student_id=int(input("Enter student_id :"))
        amount=int(input("Enter amount :"))
        payment_date=input("Enter date :")
        payment_id=int(input("Enter payment ID :"))
        stmt = self.conn.cursor()
        stmt.execute("UPDATE payments SET student_id= %s, amount= %s, payment_date= %s WHERE payment_id=%s",
                            (student_id,amount,payment_date,payment_id))
        self.conn.commit()
        print("payment updated successfully!")


    def get_payment(self) -> None:
        payment_id=int(input("Enter payment ID :"))
        stmt = self.conn.cursor()
        stmt.execute("SELECT * FROM payments WHERE payment_id= %s", (payment_id,))
        row = stmt.fetchone()
        if row:
            payment_id,student_id,amount,payment_date= row
            print(f"payment ID: {payment_id}")
            print(f"student_id: {student_id}")
            print(f"amount: {amount}")
            print(f"payment_date: {payment_date}")
            print("Payment details retrieved successfully!")
        else:
            print("No payment found with ID:", payment_id)
            return None



    def delete_payment(self):
        payment_id=int(input("Enter payment Id :"))
        stmt = self.conn.cursor()
        stmt.execute("DELETE FROM payments WHERE payment_id= %s", (payment_id,))
        self.conn.commit()
        print("payment deleted successfully!")

    def get_all_payments(self) -> List[Payment]:
        stmt = self.conn.cursor()
        stmt.execute("SELECT * FROM payments")
        payments = [Payment(*row) for row in stmt.fetchall()]
        if payments:
            print("All courses:")
            for payment in payments:
                print(f"payment ID: {payment.get_payment_id()}")
                print(f"student_id: {payment.get_student_id()}")
                print(f"amount: {payment.get_amount()}")
                print(f"payment_date: {payment.get_payment_date()}")
                print()
            print("All payments retrieved successfully!")
        else:
            print("No teachers found.")
        return payments