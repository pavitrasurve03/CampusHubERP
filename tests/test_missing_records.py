
from app.services.student_service import StudentService
from app.services.course_service import CourseService


def test_student_not_found():
    service = StudentService()

    result = service.get_student("ST999")

    assert result is None


def test_course_not_found():
    service = CourseService()

    result = service.get_course("CS999")

    assert result is None
