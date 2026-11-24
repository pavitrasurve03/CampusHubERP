
from app.services.faculty_service import FacultyService


def test_add_faculty():
    service = FacultyService()

    faculty = service.add_faculty(
        "Test Faculty", 35,
        "pytest.faculty1@gmail.com",
        "Computer Science"
    )

    assert faculty is not None
    assert faculty.faculty_id.startswith("FC")

    service.remove_faculty(faculty.faculty_id)


def test_update_faculty():
    service = FacultyService()

    faculty = service.add_faculty(
        "Update Faculty", 36,
        "pytest.faculty2@gmail.com",
        "Computer Science"
    )

    service.update_faculty(
        faculty.faculty_id,
        department="Information Technology"
    )

    updated = service.get_faculty(faculty.faculty_id)

    assert updated.department == "Information Technology"

    service.remove_faculty(faculty.faculty_id)


def test_delete_faculty():
    service = FacultyService()

    faculty = service.add_faculty(
        "Delete Faculty", 37,
        "pytest.faculty3@gmail.com",
        "Computer Science"
    )

    assert service.remove_faculty(faculty.faculty_id) is True
    assert service.get_faculty(faculty.faculty_id) is None


def test_search_faculty():
    service = FacultyService()

    faculty = service.add_faculty(
        "Search Faculty", 38,
        "pytest.faculty4@gmail.com",
        "Artificial Intelligence"
    )

    results = service.list_faculty()

    assert any(
        item.faculty_id == faculty.faculty_id
        for item in results
    )

    service.remove_faculty(faculty.faculty_id)
