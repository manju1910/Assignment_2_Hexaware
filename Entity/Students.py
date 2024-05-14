
class Student:

    def __init__(self, student_id: int, first_name: str, last_name: str, date_of_birth, email: str, phone_number: str):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone_number = phone_number
        self.enrolled_courses = []
        self.payment_history = []