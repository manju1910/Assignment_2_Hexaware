from datetime import datetime
from typing import List

class Students:
    def __init__(self, student_id: int, first_name: str, last_name: str, date_of_birth: datetime, email: str, phone_number: str):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone_number = phone_number
        self.enrolled_courses = []
        self.payment_history = []
   
    def enroll_in_course(self, course):
        self.enrolled_courses.append(course)
        

    def update_student_info(self, first_name: str, last_name: str, date_of_birth: datetime, email: str, phone_number: str):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone_number = phone_number
        

    def make_payment(self, amount: float, payment_date: datetime):
        self.payment_history.append((amount, payment_date))
       

    def display_student_info(self):
        print("Student Information:")
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Date of Birth: {self.date_of_birth.strftime('%Y-%m-%d')}")
        print(f"Email: {self.email}")
        print(f"Phone Number: {self.phone_number}")

    def get_enrolled_courses(self):
        return self.enrolled_courses

    def get_payment_history(self):
        return self.payment_history


class Courses:
    def __init__(self, course_id: int, course_name: str, course_code: str, instructor_name: str):
        self.course_id = course_id
        self.course_name = course_name
        self.course_code = course_code
        self.instructor_name = instructor_name
        self.teacher = None
        self.enrollments = []

    def assign_teacher(self, teacher):
        self.teacher = teacher
       

    def update_course_info(self, course_code: str, course_name: str, instructor: str):
        self.course_code = course_code
        self.course_name = course_name
        self.instructor_name = instructor
   

    def display_course_info(self):
        print("Course Information:")
        print(f"Course ID: {self.course_id}")
        print(f"Course Name: {self.course_name}")
        print(f"Course Code: {self.course_code}")
        print(f"Instructor Name: {self.instructor_name}")

    def get_enrollments(self):
        return self.enrollments

    def get_teacher(self):
        return self.teacher


class Enrollments:
    def __init__(self, enrollment_id: int, student_id: int, course_id: int, enrollment_date: datetime):
        self.enrollment_id = enrollment_id
        self.student_id = student_id
        self.course_id = course_id
        self.enrollment_date = enrollment_date

    def set_student(self, student:Students):
        self.student = student

    def get_student(self):
        return self.student
    
    def set_course(self,course:Courses):
        self.course = course
    
    def get_course(self):
        return self.course


class Teacher:
    def __init__(self, teacher_id: int, first_name: str, last_name: str, email: str):
        self.teacher_id = teacher_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.assigned_courses = []

    def update_teacher_info(self,teacher_id, first_name: str,last_name:str, email: str, expertise: str):
        self.first_name=first_name
        self.teacher_id=teacher_id
        self.last_name=last_name
        self.email = email
        self.expertise = expertise
      

    def display_teacher_info(self):
        print("Teacher Information:")
        print(f"Teacher ID: {self.teacher_id}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Expertise: {self.expertise}")

    def set_assigned_course(self, course):
        self.course = course

    def get_assigned_courses(self):
        return self.assigned_courses

          
class Payments:
    def __init__(self, payment_id: int, student_id: int, amount:int, payment_date: datetime):
        self.payment_id = payment_id
        self.student_id = student_id
        self.amount = amount
        self.payment_date = payment_date


    def set_student(self, student:Students):
        self.student = student

    def get_student(self):
        return self.student
    
    def get_payment_amount(self):
        return self.amount
    
    def get_payment_date(self):
        return self.payment_date
     

