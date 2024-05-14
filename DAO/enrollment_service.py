class EnrollmentService:
    
    def set_student(self, student:Students):
        self.student = student

    def get_student(self):
        return self.student
    
    def set_course(self,course:Courses):
        self.course = course
    
    def get_course(self):
        return self.course