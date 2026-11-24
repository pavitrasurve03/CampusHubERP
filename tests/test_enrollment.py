
from app.models import enrollment
from app.models import course
from app.services.student_service import StudentService
from app.services.course_service import CourseService
from app.services.enrollment_service import EnrollmentService


def test_create_enrollment():
    students = StudentService()
    courses = CourseService()
    enrollments = EnrollmentService()

    student = students.add_student(
        "Enrollment Test Student", 20,
        "pytest.enrollment@gmail.com",
        "Computer Science"
    )

    course = courses.add_course(
        "Enrollment Test Course", 4
    )

    enrollment = enrollments.enroll_student(
        student, course
    )

    assert enrollment is not None
    assert enrollment.student.student_id == student.student_id
    assert enrollment.course.course_code == course.course_code

    enrollments.remove_enrollment(enrollment.enrollment_id)
    students.remove_student(student.student_id)
    courses.remove_course(course.course_code)


def test_duplicate_enrollment():
    students = StudentService()
    courses = CourseService()
    enrollments = EnrollmentService()

    student = students.add_student(
        "Duplicate Test Student", 20,
        "pytest.duplicate@gmail.com",
        "Computer Science"
    )

    course = courses.add_course(
        "Duplicate Test Course", 3
    )

    first = enrollments.enroll_student(student, course)
    second = enrollments.enroll_student(student, course)

    assert first is not None
    assert second is None

    enrollments.remove_enrollment(first.enrollment_id)
    students.remove_student(student.student_id)
    courses.remove_course(course.course_code)


def test_delete_enrollment():
    students = StudentService()
    courses = CourseService()
    enrollments = EnrollmentService()

    student = students.add_student(
        "Delete Enrollment Student", 20,
        "pytest.deleteenrollment@gmail.com",
        "Computer Science"
    )

    course = courses.add_course(
        "Delete Enrollment Course", 3
    )

    enrollment = enrollments.enroll_student(student, course)

    result = enrollments.remove_enrollment(
        enrollment.enrollment_id
    )

    assert result is True

    remaining = enrollments.list_enrollments()

    assert not any(
        item.enrollment_id == enrollment.enrollment_id
        for item in remaining
    )

    students.remove_student(student.student_id)
    courses.remove_course(course.course_code)
