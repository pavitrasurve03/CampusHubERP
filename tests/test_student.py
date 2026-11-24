
import pytest

from app.services.student_service import StudentService


@pytest.fixture
def service():
    return StudentService()


def test_add_student(service):
    student = service.add_student(
        name="Test Student",
        age=19,
        email="pytest.student1@gmail.com",
        department="Computer Science"
    )

    assert student is not None
    assert student.student_id.startswith("ST")
    assert service.get_student(student.student_id) is not None

    service.remove_student(student.student_id)


def test_update_student(service):
    student = service.add_student(
        "Update Student", 20,
        "pytest.student2@gmail.com",
        "Computer Science"
    )

    service.update_student(
        student.student_id,
        department="Information Technology"
    )

    updated = service.get_student(student.student_id)

    assert updated.department == "Information Technology"

    service.remove_student(student.student_id)


def test_delete_student(service):
    student = service.add_student(
        "Delete Student", 21,
        "pytest.student3@gmail.com",
        "Computer Science"
    )

    result = service.remove_student(student.student_id)

    assert result is True
    assert service.get_student(student.student_id) is None


def test_search_student(service):
    student = service.add_student(
        "Search Student", 19,
        "pytest.student4@gmail.com",
        "Artificial Intelligence"
    )

    results = service.list_students(
        department="Artificial Intelligence"
    )

    assert any(
        item.student_id == student.student_id
        for item in results
    )

    service.remove_student(student.student_id)
