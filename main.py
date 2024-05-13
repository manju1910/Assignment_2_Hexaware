from datetime import datetime
from student import Student
from course import Course
from teacher import Teacher
from enrollment import Enrollment
from payment import Payment
from sis import SIS

def main():
    # Create instances of classes
    student1 = Student(1, "John", "Doe", datetime(1995, 8, 15), "john.doe@example.com", "1234567890")
    course1 = Course(1, "Mathematics", "MATH101", "Dr. Smith")
    #teacher1 = Teacher(1, "Dr. Smith", "Mathematics", "smith@example.com")
    sis = SIS()

    # Add enrollment
    sis.add_enrollment(student1, course1, datetime.now())

    # Assign course to teacher
    sis.assign_course_to_teacher(course1, teacher1)

    # Add payment
    sis.add_payment(student1, 100, datetime.now())

    # Get enrollments for student
    enrollments = sis.get_enrollments_for_student(student1)
    for enrollment in enrollments:
        print(f"Enrollment ID: {enrollment.enrollment_id}, Course ID: {enrollment.course_id}")

    # Get courses for teacher
    courses = sis.get_courses_for_teacher(teacher1)
    for course in courses:
        print(f"Course ID: {course.course_id}, Course Name: {course.course_name}")

if __name__ == "__main__":
    main()
