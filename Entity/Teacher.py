class Teacher:
    def __init__(self, teacher_id: int, first_name: str, last_name: str, email: str):
        self.teacher_id = teacher_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.assigned_courses = []