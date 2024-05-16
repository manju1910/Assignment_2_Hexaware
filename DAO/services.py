from abc import ABC, abstractmethod
from typing import List
from Entity.Student import Student
from Entity.Course import Course
from Entity.Enrollment import Enrollment
from Entity.Teacher import Teacher
from Entity.Payment import Payment


class StudentDAO(ABC):
    @abstractmethod
    def add_student(self):
        pass

    @abstractmethod
    def update_student(self):
        pass

    @abstractmethod
    def get_student(self):
        pass

    @abstractmethod
    def delete_student(self):
        pass

    @abstractmethod
    def get_all_students(self) -> List[Student]:
        pass


class CourseDAO(ABC):
    @abstractmethod
    def add_course(self):
        pass

    @abstractmethod
    def update_course(self):
        pass

    @abstractmethod
    def get_course(self):
        pass

    @abstractmethod
    def delete_course(self):
        pass

    @abstractmethod
    def get_all_courses(self) -> List[Course]:
        pass


class EnrollmentDAO(ABC):
    @abstractmethod
    def add_enrollment(self):
        pass

    @abstractmethod
    def update_enrollment(self):
        pass

    @abstractmethod
    def get_enrollment(self):
        pass

    @abstractmethod
    def delete_enrollment(self):
        pass

    @abstractmethod
    def get_all_enrollments(self) -> List[Enrollment]:
        pass


class TeacherDAO(ABC):
    @abstractmethod
    def add_teacher(self):
        pass

    @abstractmethod
    def update_teacher(self):
        pass

    @abstractmethod
    def get_teacher(self):
        pass

    @abstractmethod
    def delete_teacher(self):
        pass

    @abstractmethod
    def get_all_teachers(self) -> List[Teacher]:
        pass


class PaymentDAO(ABC):
    @abstractmethod
    def add_payment(self):
        pass

    @abstractmethod
    def update_payment(self):
        pass

    @abstractmethod
    def get_payment(self):
        pass

    @abstractmethod
    def delete_payment(self):
        pass

    @abstractmethod
    def get_all_payments(self) -> List[Payment]:
        pass
