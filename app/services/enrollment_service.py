from app.utils.logger import log_info, log_error
from app.models.enrollment import Enrollment
from app.database.repository import repository

from app.utils.decorators import log_decorator, time_decorator


class EnrollmentService:

    def __init__(self):
        self.repository = repository
        self.counter = 0

    @property
    def enrollments(self):
        return self.repository.get_enrollments()

    @log_decorator
    @time_decorator
    def enroll_student(self, student, course):

        # Check for an existing student-course combination
        for enrollment in self.enrollments:

            if (
                enrollment.student.student_id == student.student_id
                and enrollment.course.course_code == course.course_code
            ):
                print("Student is already enrolled in this course!")
                return None

        self.counter += 1
        enrollment_id = f"EN{self.counter:03d}"

        # Avoid duplicate enrollment IDs after restarting
        while self.repository.get_enrollment(enrollment_id) is not None:
            self.counter += 1
            enrollment_id = f"EN{self.counter:03d}"

        enrollment = Enrollment(
            enrollment_id,
            student,
            course
        )

        self.repository.add_enrollment(enrollment)
        log_info(f"Enrollment Created: {enrollment.enrollment_id}")
        print("Student enrolled successfully!")
        return enrollment

    @log_decorator
    @time_decorator
    def remove_enrollment(self, enrollment_id):

        result = self.repository.delete_enrollment(enrollment_id)
        log_info(f"Enrollment Deleted: {enrollment_id}")
        if result:
            print("Enrollment removed successfully!")
            return True

        print("Enrollment not found!")
        return False

    @log_decorator
    @time_decorator
    def list_enrollments(self):

        enrollments = self.enrollments

        print("\n--- ENROLLMENT LIST ---")

        if not enrollments:
            print("No enrollment records found.")

        else:
            for enrollment in enrollments:
                print(
                    f"ID: {enrollment.enrollment_id} | "
                    f"Student: {enrollment.student.name} | "
                    f"Course: {enrollment.course.course_name}"
                )

        return enrollments
