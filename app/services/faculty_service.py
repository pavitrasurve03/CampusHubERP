
from app.core.validators import (
    validate_email,
    validate_faculty_id
)

from app.models.faculty import Faculty
from app.database.repository import repository
from app.utils.logger import log_info, log_error
from app.utils.generators import generate_faculty_id
from app.utils.decorators import log_decorator, time_decorator


class FacultyService:

    def __init__(self):
        self.repository = repository

    @property
    def faculties(self):
        return self.repository.get_faculty()

    @log_decorator
    @time_decorator
    def add_faculty(self, name, age, email, department):

        faculty_id = generate_faculty_id()

        while self.repository.get_faculty_by_id(faculty_id) is not None:
            faculty_id = generate_faculty_id()

        if not validate_faculty_id(faculty_id):
            raise ValueError("Invalid Faculty ID!")

        if not validate_email(email):
            raise ValueError("Invalid Email Address!")

        faculty = Faculty(
            faculty_id=faculty_id,
            name=name,
            age=age,
            email=email,
            department=department
        )

        self.repository.add_faculty(faculty)
        log_info(f"Faculty Added: {faculty.faculty_id}")
        print("Faculty added successfully!")
        return faculty

    @log_decorator
    @time_decorator
    def remove_faculty(self, faculty_id):

        result = self.repository.delete_faculty(faculty_id)
        log_info(f"Faculty Deleted: {faculty_id}")
        if result:
            print("Faculty removed successfully!")
            return True

        print("Faculty not found!")
        return False

    @log_decorator
    @time_decorator
    def update_faculty(self, faculty_id, **kwargs):

        allowed_fields = {
            "name", "age", "email", "department"
        }

        for key, value in kwargs.items():
            if key not in allowed_fields:
                raise ValueError(f"Invalid field: {key}")

        faculty = self.repository.get_faculty_by_id(faculty_id)

        if faculty is None:
            print("Faculty not found!")
            return None

        if "email" in kwargs and not validate_email(kwargs["email"]):
            raise ValueError("Invalid Email Address!")

        for key, value in kwargs.items():
            setattr(faculty, key, value)

        faculty.touch()

        updated = self.repository.update_faculty(
            faculty_id,
            **kwargs,
            updated_at=faculty.updated_at
        )
        log_info(f"Faculty Updated: {faculty_id}")
        print("Faculty updated successfully!")
        return updated

    @log_decorator
    @time_decorator
    def list_faculty(self):

        faculties = sorted(
            self.faculties,
            key=lambda faculty: faculty.name.lower()
        )

        print("\n--- FACULTY LIST ---")

        if not faculties:
            print("No faculty records found.")

        else:
            for faculty in faculties:
                print(
                    f"ID: {faculty.faculty_id} | "
                    f"Name: {faculty.name} | "
                    f"Department: {faculty.department}"
                )

        return faculties

    def get_faculty(self, faculty_id):
        return self.repository.get_faculty_by_id(faculty_id)