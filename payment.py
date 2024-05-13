from datetime import datetime

class Payment:
    def __init__(self, payment_id: int, student_id: int, amount: int, payment_date: datetime):
        self.payment_id = payment_id
        self.student_id = student_id
        self.amount = amount
        self.payment_date = payment_date


    def set_student(self, student):
        self.student = student

    def get_student(self):
        return self.student
    
    def get_payment_amount(self):
        return self.amount
    
    def get_payment_date(self):
        return self.payment_date
