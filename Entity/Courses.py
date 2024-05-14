class Courses:
    def __init__(self, course_id: int, course_name: str, course_code: str, instructor_name: str):
        self.course_id = course_id
        self.course_name = course_name
        self.course_code = course_code
        self.instructor_name = instructor_name
        self.teacher = None
        self.enrollments = []