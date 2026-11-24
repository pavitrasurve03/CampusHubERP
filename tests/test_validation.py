
from app.core.validators import (
    validate_email,
    validate_student_id,
    validate_faculty_id,
    validate_course_code
)


def test_invalid_email():
    assert validate_email("invalid-email") is False


def test_valid_email():
    assert validate_email("student@gmail.com") is True


def test_invalid_student_id():
    assert validate_student_id("ABC123") is False


def test_invalid_faculty_id():
    assert validate_faculty_id("ST001") is False


def test_invalid_course_code():
    assert validate_course_code("INVALID") is False


def test_valid_course_code():
    assert validate_course_code("CS101") is True
