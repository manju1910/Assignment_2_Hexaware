import pyodbc
from typing import List
from DAO.course_service import CourseService
from DAO.enrollment_service import EnrollmentService
from DAO.payment_service import PaymentService
from DAO.student_service import StudentService
from DAO.teacher_service import TeacherService
from Entity import Courses
from Entity import Enrollments
from Entity import Payments
from Entity import Students
from Entity import Teacher

 
 



class MainMenu:
    course_service=CourseService()
    enrollment_service=EnrollmentService()
    payment_service=PaymentService()
    student_service=StudentService()
    teacher_service=TeacherService()
    def course_menu(self):
      
    
        while True:
            print(
                """      
            1. Add a Course
            2. Assign Teacher
            3. UpdateCourseInfo 
            4.DisplayCourseInfo
            5.AssignTeacherToCourse
            6.CalculateCourseStatistics
            7.AssignCourseToTeacher
            8. Back to main menu
                    """
            )
            choice = int(input("Please choose from above options: "))
    
            if choice == 1:
                course_id=int(input("Enter course id: "))
                course_name= input("Enter the course name: ") 
                credits=int(input("Enter the credits: ")) 
                teacher_id=int(input("Enter the teacher id: "))
                new_course = Courses(course_id, course_name, credits, teacher_id)
                self.course_service.create_course(new_course)
            elif choice == 2:
                course_id=int(input("Enter course id: "))
                course_name= input("Enter the course name: ") 
                credits=int(input("Enter the credits: ")) 
                teacher_id=int(input("Enter the teacher id: "))
                new_course = Courses(course_id, course_name, credits, teacher_id)
                self.course_service.assign_teacher(new_course)
            elif choice == 3:
                course_id=int(input("Enter course id: "))
                credits= int(input("Enter the credits: ") )
                new_course = Courses(course_id,credits)  
                self.course_service.update_course(new_course)
            elif choice == 4:
                course_id = int(input("Please tell a course id: "))
                self.course_service.display_course_info(course_id)
            elif choice == 5:
                course_id=int(input("Enter course id: "))
                course_name= input("Enter the course name: ") 
                credits=int(input("Enter the credits: ")) 
                teacher_id=int(input("Enter the teacher id: "))
                new_course = Courses(course_id, course_name, credits, teacher_id)
                self.course_service.assign_teacher_to_course(new_course)
            elif choice == 6:
                course_id=int(input("Enetr the course id to calculate statistics: ")) 
                course_name=input("Enter thee course name: ")
                new_course=Courses(course_id,course_name)
                self.course_service.calculate_course_statistics(new_course)
            elif choice == 7:
                course_id=int(input("Enter course id: "))
                course_name= input("Enter the course name: ") 
                credits=int(input("Enter the credits: ")) 
                teacher_id=int(input("Enter the teacher id: "))
                new_course = Courses(course_id, course_name, credits, teacher_id)
                self.course_service.assign_course_to_teacher(new_course) 
                              
            elif choice == 8:
                break
    
    
    def enrollment_menu(self):
        while True:
            print(
                """      
            1. EnrollInCourse
            2. Get Enrolled Course to specific student
            3. Get Enrollment for specific course 
            4.Student Associated with the enrollment
            5.Course Associated with the enrollment
            6.Enroll Student In Course
            7.Generate Enrollments report
            8.Add Enrollments
            9.Get Enrollment for student
            10. Back to main menu
                    """
            )
            choice = int(input("Please choose from above options: "))
    
            if choice == 1:
                enrollment_id=int(input("Enter the enrollment id: "))
                student_id=int(input("Enter the student id: "))
                course_id=int(input("enter the course id: ")) 
                enrollment_date=int(input("Enter the enrollment date: "))
                new_course = Courses(enrollment_id, student_id, course_id, enrollment_date)
                self.course_service.enroll_in_course(new_course)
            elif choice == 2:
                student_id=int(input("Enter the student id: "))
                new_course = Courses(student_id)
                self.course_service.enrolled_specific_student(new_course)
            elif choice == 3:
                course_id=int(input("Enter course id: "))
                new_course = Courses(course_id)  
                self.course_service.enrolled_specific_course(new_course)
            elif choice == 4:     
                self.course_service.student_associated_enrollment()
            elif choice == 5:
                 self.course_service.course_associated_enrollment()
            elif choice == 6:
                enrollment_id=int(input("Enter the enrollment id: "))
                student_id=int(input("Enter the student id: "))
                course_id=int(input("enter the course id: ")) 
                enrollment_date=int(input("Enter the enrollment date: "))
                new_course = Courses(enrollment_id, student_id, course_id, enrollment_date)
                self.course_service.enroll_student_in_course(new_course)
            elif choice == 7:
                course_id=int(input("Enter course id: "))              
                new_course = Courses(course_id)
                self.course_service.generate_enrollment_report(new_course) 
                              
            elif choice ==8: 
                enrollment_id=int(input("Enter the enrollment id: "))
                student_id=int(input("Enter the student id: "))
                course_id=int(input("enter the course id: ")) 
                enrollment_date=int(input("Enter the enrollment date: "))
                new_course = Courses(enrollment_id, student_id, course_id, enrollment_date)
                self.course_service.add_enrollment(new_course)  
            elif choice ==9:
                student_id=int(input("Enter the student id: "))
                self.course_service.get_enrollment_for_student(student_id)                    
            elif choice == 10:
                break
    
    def payment_menu(self):

        while True:
            print(
                """      
            1. Make Payment
            2. Get total payment for specific student
            3. Get Payment amount
            4.Get Payment date
            5.Record the payment made by student
            6.Generate payment report
            7.Add Payments
            8. Back to main menu
                    """
            )
            choice = int(input("Please choose from above options: "))
    
            if choice == 1:
               payment_id=int(input("enter the payment id: "))
               student_id=int(input("Enter the student id: ")) 
               amount=int(input("Enter the total amount: "))
               payment_date=input("Enter the payment date: ")
               new_course = Payments(payment_id ,student_id,amount,payment_date)
               self.course_service.make_payment(new_course)
            elif choice == 2:
                student_id=int(input("Enter the student id: "))
                new_course = Payments(student_id)
                self.course_service.get_payment_student(new_course)
            elif choice == 3:
                course_id=int(input("Enter course id: "))
                new_course = Payments(course_id)  
                self.course_service.payment_student(new_course)
            elif choice == 4:
                course_id=int(input("Enter course id: "))
                new_course = Payments(course_id)     
                self.course_service.payment_date(new_course)
            elif choice == 5:
                 payment_id=int(input("enter the payment id: "))
                 student_id=int(input("Enter the student id: ")) 
                 amount=int(input("Enter the total amount: "))
                 payment_date=input("Enter the payment date: ")
                 new_course = Payments(payment_id ,student_id,amount,payment_date)
                 self.course_service.record_payment()
            elif choice == 6:
                student_id=int(input("enter the student id: "))
                self.course_service.payment_report(student_id)
            elif choice == 7:
                payment_id=int(input("enter the payment id: "))
                student_id=int(input("Enter the student id: ")) 
                amount=int(input("Enter the total amount: "))
                payment_date=input("Enter the payment date: ")
                new_course = Payments(payment_id ,student_id,amount,payment_date)
                self.course_service.add_payment(new_course)                 
            elif choice == 8:
                break
    def student_menu(self):
        while True:
            print(
                """      
            1. Make Payment
            2. Get total payment for specific student
            3. Get Payment amount
            4.Get Payment date
            5.Record the payment made by student
            6.Generate payment report
            7.Add Payments
            8. Back to main menu
                    """
            )
            choice = int(input("Please choose from above options: "))
    
            if choice == 1:
               payment_id=int(input("enter the payment id: "))
               student_id=int(input("Enter the student id: ")) 
               amount=int(input("Enter the total amount: "))
               payment_date=input("Enter the payment date: ")
               new_course = Payments(payment_id ,student_id,amount,payment_date)
               self.course_service.make_payment(new_course)
            elif choice == 2:
                student_id=int(input("Enter the student id: "))
                new_course = Payments(student_id)
                self.course_service.get_payment_student(new_course)
            elif choice == 3:
                course_id=int(input("Enter course id: "))
                new_course = Payments(course_id)  
                self.course_service.payment_student(new_course)
            elif choice == 4:
                course_id=int(input("Enter course id: "))
                new_course = Payments(course_id)     
                self.course_service.payment_date(new_course)
            elif choice == 5:
                 payment_id=int(input("enter the payment id: "))
                 student_id=int(input("Enter the student id: ")) 
                 amount=int(input("Enter the total amount: "))
                 payment_date=input("Enter the payment date: ")
                 new_course = Payments(payment_id ,student_id,amount,payment_date)
                 self.course_service.record_payment()
            elif choice == 6:
                student_id=int(input("enter the student id: "))
                self.course_service.payment_report(student_id)
            elif choice == 7:
                payment_id=int(input("enter the payment id: "))
                student_id=int(input("Enter the student id: ")) 
                amount=int(input("Enter the total amount: "))
                payment_date=input("Enter the payment date: ")
                new_course = Payments(payment_id ,student_id,amount,payment_date)
                self.course_service.add_payment(new_course)                 
            elif choice == 8:
                break
    def teacher_menu(self):
        pass
 
# Task 5 - Keep it in loop
if __name__ == "__main__":
    print("Welcome to Student Information System")
    main_menu=MainMenu()
    while True:
        print(
            """      
            1. Course Management
            2. Enrollment Management
            3. Payment Management
            4. Student Management
            5. Teacher Management
            6. Exit
                """
        )
 
        choice = int(input("Please choose from above options: "))
 
        if choice == 1:
            main_menu.course_menu()
        elif choice == 2:
            main_menu.enrollment_menu()
        elif choice == 3:
            main_menu.payment_menu()
        elif choice == 4:
            main_menu.student_menu() 
        elif choice == 5:
            main_menu.teacher_menu()        
        elif choice == 6:
            main_menu.course_service.close()
            
            break
 
   






          


