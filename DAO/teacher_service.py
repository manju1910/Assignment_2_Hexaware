class TeacherService:
  
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
