from dao.servicesImpl import StudentServiceImpl, CourseServiceImpl, EnrollmentServiceImpl, TeacherServiceImpl, PaymentServiceImpl
from Exception.myexceptions import InvalidDataException
from Entity.Student import Student
from Entity.Course import Course
from Entity.Enrollment import Enrollment
from Entity.Payment import Payment
from Entity.Teacher import Teacher
from datetime import datetime



class Main:
    def _init_(self):
        self.loop = None

    def main(self):
        self.loop = True
        while self.loop:
            try:
                student_service = StudentServiceImpl()
                course_service = CourseServiceImpl()
                enrollment_service = EnrollmentServiceImpl()
                teacher_service = TeacherServiceImpl()
                payment_service= PaymentServiceImpl()
                print("Welcome to Student Information System!!!")
                print("Select option to use functionalities: ")
                print("1.Student\n2.Course\n3.Enrollment\n4.Teacher\n5.Payment\n6.Exit")
                choice = int(input("Enter your choice: "))
                if choice in range(1, 7):
                    if choice == 1:
                        while True:
                            print('''1.enroll student\n2.Update student\n3.Get Student\n4.Delete Student
5.Get all students\n6.Exit''')
                            choice_1 = int(input("Enter your Choice: "))
                            if choice_1 in range(1, 7):
                                if choice_1 == 1:
                                    student_service.add_student()
                                elif choice_1 == 2:
                                    student_service.update_student()
                                elif choice_1 == 3:
                                    student_service.get_student()
                                elif choice_1 == 4:
                                    student_service.delete_student()
                                elif choice_1 == 5:
                                    student_service.get_all_students()
                                else:
                                    break
                            else:
                                raise InvalidDataException("Input should be between 1 and 6")
                    elif choice == 2:
                        while True:
                            print('''1.add course\n2.update course\n3.get course\n4.delete course
5.get all courses\n6.Exit''')
                            choice_2 = int(input("Enter your Choice: "))
                            if choice_2 in range(1, 7):
                                if choice_2 == 1:
                                    course_service.add_course()
                                elif choice_2 == 2:
                                    course_service.update_course()
                                elif choice_2 == 3:
                                    course_service.get_course()
                                elif choice_2 == 4:
                                    course_service.delete_course()
                                elif choice_2 == 5:
                                    course_service.get_all_courses()
                                else:
                                    break
                            else:
                                raise InvalidDataException("Input should be between 1 and 6")
                    elif choice == 3:
                        while True:
                            print('''1.add enrollments\n2.update enrollments\n3.get enrollments\n4.delete enrollments
5.get all enrollments\n6.Exit''')
                            choice_3 = int(input("Enter your Choice: "))
                            if choice_3 in range(1, 7):
                                if choice_3 == 1:
                                    enrollment_service.add_enrollment()
                                elif choice_3 == 2:
                                    enrollment_service.update_enrollment()
                                elif choice_3 == 3:
                                    enrollment_service.get_enrollment()
                                elif choice_3 == 4:
                                    enrollment_service.delete_enrollment()
                                elif choice_3 == 5:
                                    enrollment_service.get_all_enrollments()
                                else:
                                    break
                            else:
                                raise InvalidDataException("Input should be between 1 and 6")
                    elif choice == 4:
                        while True:
                            print('''1.add teacher\n2.Update teacher\n3.get teacher\n4.delete teacher
5.get all teachers\n6.Exit''')
                            choice_4 = int(input("Enter your Choice: "))
                            if choice_4 in range(1, 7):
                                if choice_4 == 1:
                                    teacher_service.add_teacher()
                                elif choice_4 == 2:
                                    teacher_service.update_teacher()
                                elif choice_4 == 3:
                                    teacher_service.get_teacher()
                                elif choice_4 == 4:
                                    teacher_service.delete_teacher()
                                elif choice_4 == 5:
                                    teacher_service.get_all_teachers()
                                else:
                                    break
                            else:
                                raise InvalidDataException("Input should be between 1 and 6")
                    elif choice == 5:
                        while True:
                            print('''1.add payment\n2.Update payment\n3.get payment\n4.delete payment
5.get all payments\n6.Exit''')
                            choice_5 = int(input("Enter your Choice: "))
                            if choice_5 in range(1, 7):
                                if choice_5 == 1:
                                    payment_service.add_payment()
                                elif choice_5 == 2:
                                    payment_service.update_payment()
                                elif choice_5 == 3:
                                    payment_service.get_payment()
                                elif choice_5 == 4:
                                    payment_service.delete_payment()
                                elif choice_5 == 5:
                                    payment_service.get_all_payments()
                                else:
                                    break
                            else:
                                raise InvalidDataException("Input should be between 1 and 6")
                    else:
                        exit()
            except Exception as e:
                print(f"An error occurred: {e}")
            finally:
                print("Thank You for reaching Student Information System...")



obj = Main()
obj.main()
