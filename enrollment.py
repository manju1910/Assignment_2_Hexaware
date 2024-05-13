from datetime import datetime

class DuplicateEnrollmentException(Exception):
    pass

class CourseNotFoundException(Exception):
    pass

class Enrollment:
    def __init__(self, enrollment_id: int, student_id: int, course_id: int, enrollment_date: datetime):
        self.enrollment_id = enrollment_id
        self.student_id = student_id
        self.course_id = course_id
        self.enrollment_date = enrollment_date

    def set_student(self, student):
        self.student = student

    def get_student(self):
        return self.student
    
    def set_course(self, course):
        self.course = course
    
    def get_course(self):
        return self.course
