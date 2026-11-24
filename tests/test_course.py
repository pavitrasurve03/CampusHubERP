
from app.services.course_service import CourseService


def test_add_course():
    service = CourseService()

    course = service.add_course(
        "Testing Python Course", 4
    )

    assert course is not None
    assert course.course_code.startswith("CS")

    service.remove_course(course.course_code)


def test_update_course():
    service = CourseService()

    course = service.add_course(
        "Old Test Course", 3
    )

    service.update_course(
        course.course_code,
        course_name="Updated Test Course",
        credits=4
    )

    updated = service.get_course(course.course_code)

    assert updated.course_name == "Updated Test Course"
    assert updated.credits == 4

    service.remove_course(course.course_code)


def test_delete_course():
    service = CourseService()

    course = service.add_course(
        "Delete Test Course", 3
    )

    assert service.remove_course(course.course_code) is True
    assert service.get_course(course.course_code) is None


def test_search_course():
    service = CourseService()

    course = service.add_course(
        "Search Test Course", 4
    )

    results = service.list_courses()

    assert any(
        item.course_code == course.course_code
        for item in results
    )

    service.remove_course(course.course_code)
