
from app.core.validators import (
    validate_email,
    validate_student_id
)

from app.models.student import Student
from app.database.repository import repository
from app.utils.logger import log_info, log_error
from app.utils.generators import generate_student_id
from app.utils.decorators import log_decorator, time_decorator


class StudentService:

    def __init__(self):
        self.repository = repository

    @property
    def students(self):
        return self.repository.get_students()

    @log_decorator
    @time_decorator
    def add_student(self, name, age, email, department):

        student_id = generate_student_id()

        # Avoid duplicate IDs after restarting the application
        while self.repository.get_student(student_id) is not None:
            student_id = generate_student_id()

        if not validate_student_id(student_id):
            raise ValueError("Invalid Student ID!")

        if not validate_email(email):
            raise ValueError("Invalid Email Address!")

        student = Student(
            student_id=student_id,
            name=name,
            age=age,
            email=email,
            department=department
        )

        self.repository.add_student(student)
        log_info(f"Student Added: {student.student_id}")
        print("Student added successfully!")
        return student

    @log_decorator
    @time_decorator
    def remove_student(self, student_id):

        result = self.repository.delete_student(student_id)
        log_info(f"Student Deleted: {student_id}")
        if result:
            print("Student removed successfully!")
            return True
        
        print("Student not found!")
        return False

    @log_decorator
    @time_decorator
    def update_student(self, student_id, **kwargs):

        allowed_fields = {
            "name", "age", "email", "department"
        }

        for key, value in kwargs.items():
            if key not in allowed_fields:
                raise ValueError(f"Invalid field: {key}")

        student = self.repository.get_student(student_id)

        if student is None:
            print("Student not found!")
            return None

        if "email" in kwargs and not validate_email(kwargs["email"]):
            raise ValueError("Invalid Email Address!")

        # Use descriptors to validate name and age as well.
        for key, value in kwargs.items():
            setattr(student, key, value)

        student.touch()

        updated = self.repository.update_student(
            student_id,
            **kwargs,
            updated_at=student.updated_at
        )
        log_info(f"Student Updated: {student_id}")
        print("Student updated successfully!")
        return updated

    @log_decorator
    @time_decorator
    def list_students(self, department=None):

        students = self.students

        if department is not None:
            students = list(filter(
                lambda student:
                student.department.lower() == department.lower(),
                students
            ))

        students = sorted(
            students,
            key=lambda student: student.name.lower()
        )

        uppercase_names = list(map(
            lambda student: student.name.upper(),
            students
        ))

        print("\n--- STUDENT LIST ---")

        if not students:
            print("No students found.")

        else:
            for student, name in zip(students, uppercase_names):
                print(
                    f"ID: {student.student_id} | "
                    f"Name: {name} | "
                    f"Department: {student.department}"
                )

        return students

    def get_student(self, student_id):
        return self.repository.get_student(student_id)