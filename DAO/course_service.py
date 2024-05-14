class CourseService:
   

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