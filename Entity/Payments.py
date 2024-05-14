class Payments:
    def __init__(self, payment_id: int, student_id: int, amount:int, payment_date):
        self.payment_id = payment_id
        self.student_id = student_id
        self.amount = amount
        self.payment_date = payment_date