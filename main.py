import pyodbc
from typing import List
from DAO.course_service import CourseService
from DAO.enrollment_service import EnrollmentService
from DAO.payment_service import PaymentService
from DAO.student_service import StudentService
from DAO.teacher_service import TeacherService

 
 



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
            5.List of students enrolled to the course
            6.Teachers assigned to course
            7.AssignTeacherToCourse
            8.CalculateCourseStatistics
            9.AssignCourseToTeacher
            10. Back to main menu
                    """
            )
            choice = int(input("Please choose from above options: "))
    
            if choice == 1:
                title = input("Please enter movie title: ")
                year = int(input("Please enter movie year: "))
                director_id = int(input("Please enter movie director's id: "))
                new_movie = Movie(title, year, director_id)
                self.course_service.create_course(new_movie)
            elif choice == 2:
                self.course_service.read_movies()
            elif choice == 3:
                movie_id = int(input("Please enter movie's id: "))
                title = input("Please enter movie title: ")
                year = int(input("Please enter movie year: "))
                director_id = int(input("Please enter movie director's id: "))
                updated_movie = Movie(title, year, director_id)
                self.course_service.update_movie(updated_movie, movie_id)
            elif choice == 4:
                movie_id = int(input("Please tell a movie id to delete: "))
                self.course_service.delete_movie(movie_id)
            elif choice == 5:
                movie_id = int(input("Please tell a movie id to delete: "))
                self.course_service.delete_movie(movie_id) 
            elif choice == 6:
                movie_id = int(input("Please tell a movie id to delete: "))
                self.course_service.delete_movie(movie_id)
            elif choice == 7:
                movie_id = int(input("Please tell a movie id to delete: "))
                self.course_service.delete_movie(movie_id) 
            elif choice == 8:
                movie_id = int(input("Please tell a movie id to delete: "))
                self.course_service.delete_movie(movie_id)
            elif choice == 9:
                movie_id = int(input("Please tell a movie id to delete: "))
                self.course_service.delete_movie(movie_id)                  
            elif choice == 10:
                break
    
    
    def director_menu(self):
         while True:
            print(
                """      
            
            1. View all Movies
            2. Back to main menu
                    """
            )
            choice = int(input("Please choose from above options: "))
    
            
            if choice == 1:
                self.director_service.read_director()
            elif choice == 2:
                break
    
    
    
    def actor_menu(self):
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
 
   






          


