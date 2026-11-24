
from app.core.validators import validate_course_code
from app.utils.logger import log_info, log_error
from app.models.course import Course
from app.database.repository import repository

from app.utils.generators import generate_course_id
from app.utils.decorators import log_decorator, time_decorator


class CourseService:

    def __init__(self):
        self.repository = repository

    @property
    def courses(self):
        return self.repository.get_courses()

    @log_decorator
    @time_decorator
    def add_course(self, course_name, credits):

        course_code = generate_course_id()

        while self.repository.get_course(course_code) is not None:
            course_code = generate_course_id()

        if not validate_course_code(course_code):
            raise ValueError("Invalid Course Code!")

        if not isinstance(course_name, str) or not course_name.strip():
            raise ValueError("Course name cannot be empty.")

        if isinstance(credits, bool) or not isinstance(credits, int) or credits <= 0:
            raise ValueError("Credits must be a positive integer.")

        course = Course(
            course_code=course_code,
            course_name=course_name.strip(),
            credits=credits
        )

        self.repository.add_course(course)
        log_info(f"Course Added: {course.course_code}")
        print("Course added successfully!")
        return course

    @log_decorator
    @time_decorator
    def remove_course(self, course_code):

        result = self.repository.delete_course(course_code)
        log_info(f"Course Deleted: {course_code}")
        if result:
            print("Course removed successfully!")
            return True

        print("Course not found!")
        return False

    @log_decorator
    @time_decorator
    def update_course(self, course_code, **kwargs):

        allowed_fields = {"course_name", "credits"}

        for key, value in kwargs.items():

            if key not in allowed_fields:
                raise ValueError(f"Invalid field: {key}")

            if key == "course_name":
                if not isinstance(value, str) or not value.strip():
                    raise ValueError("Course name cannot be empty.")

                kwargs[key] = value.strip()

            if key == "credits":
                if (
                    isinstance(value, bool)
                    or not isinstance(value, int)
                    or value <= 0
                ):
                    raise ValueError(
                        "Credits must be a positive integer."
                    )

        course = self.repository.get_course(course_code)
        log_info(f"Course Updated: {course_code}")
        if course is None:
            print("Course not found!")
            return None

        course.touch()

        updated = self.repository.update_course(
            course_code,
            **kwargs,
            updated_at=course.updated_at
        )

        print("Course updated successfully!")
        return updated

    @log_decorator
    @time_decorator
    def list_courses(self):

        courses = sorted(
            self.courses,
            key=lambda course: course.course_name.lower()
        )

        print("\n--- COURSE LIST ---")

        if not courses:
            print("No courses found.")

        else:
            for course in courses:
                print(
                    f"Code: {course.course_code} | "
                    f"Name: {course.course_name} | "
                    f"Credits: {course.credits}"
                )

        return courses

    def get_course(self, course_code):
        return self.repository.get_course(course_code)