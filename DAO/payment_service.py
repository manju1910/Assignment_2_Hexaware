class PaymentService:
   

    def set_student(self, student:Students):
        self.student = student

    def get_student(self):
        return self.student
    
    def get_payment_amount(self):
        return self.amount
    
    def get_payment_date(self):
        return self.payment_date
     