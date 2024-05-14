class StudentService:
   
    def enroll_in_course(self, course):
        self.enrolled_courses.append(course)
        

    def update_student_info(self, first_name: str, last_name: str, date_of_birth, email: str, phone_number: str):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone_number = phone_number
        

    def make_payment(self, amount: float, payment_date):
        self.payment_history.append((amount, payment_date))
       

    def display_student_info(self):
        print("Student Information:")
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Date of Birth: {self.date_of_birth}")
        print(f"Email: {self.email}")
        print(f"Phone Number: {self.phone_number}")

    def get_enrolled_courses(self):
        return self.enrolled_courses

    def get_payment_history(self):
        return self.payment_history