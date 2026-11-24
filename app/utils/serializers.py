
import json
from pathlib import Path

from app.models import faculty


# Project root and data folder
BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data"


def prepare_data_folder():

    DATA_DIR.mkdir(parents=True, exist_ok=True)


# Convert Python objects into dictionaries
def convert_to_dict(records):

    result = []

    for record in records:

        if hasattr(record, "to_dict"):
            result.append(record.to_dict())

        else:
            result.append(record)

    return result


# Save records into a JSON file
def save_json(filename, records):

    prepare_data_folder()

    file_path = DATA_DIR / filename

    data = convert_to_dict(records)

    with open(file_path, "w", encoding="utf-8") as file:

        json.dump(data, file, indent=4)

    print(f"{filename} saved successfully!")


# Load records from a JSON file
def load_json(filename):

    prepare_data_folder()

    file_path = DATA_DIR / filename

    if not file_path.exists():
        return []

    with open(file_path, "r", encoding="utf-8") as file:

        return json.load(file)


# ==========================================
# STUDENT JSON FUNCTIONS
# ==========================================

def save_Students_json(students):

    save_json("Students.json", students)


def load_Students_json():

    return load_json("Students.json")


# ==========================================
# FACULTY JSON FUNCTIONS
# ==========================================

def save_faculty_json(faculties):

    save_json("faculty.json", faculties)


def load_faculty_json():

    return load_json("faculty.json")


# ==========================================
# COURSE JSON FUNCTIONS
# ==========================================

def save_courses_json(courses):

    save_json("courses.json", courses)


def load_courses_json():

    return load_json("courses.json")


# ==========================================
# ENROLLMENT JSON FUNCTIONS
# ==========================================

def save_enrollments_json(enrollments):

    save_json("enrollments.json", enrollments)


def load_enrollments_json():

    return load_json("enrollments.json")


# ==========================================
# EXPORT ALL APPLICATION DATA
# ==========================================

def export_data(
    student_service,
    faculty_service,
    course_service,
    enrollment_service
):

    print("\n========== EXPORTING DATA ==========")

    save_Students_json(student_service.students)

    save_faculty_json(faculty_service.faculties)

    save_courses_json(course_service.courses)

    save_enrollments_json(enrollment_service.enrollments)

    print("All application data exported successfully!")


# ==========================================
# IMPORT ALL APPLICATION DATA
# ==========================================


def import_data(
    student_service,
    faculty_service,
    course_service,
    enrollment_service
):
    from app.models.student import Student
    from app.models.faculty import Faculty
    from app.models.course import Course
    from app.models.enrollment import Enrollment

    from app.core.validators import (
        validate_email,
        validate_student_id,
        validate_faculty_id,
        validate_course_code
    )

    print("\n========== IMPORTING DATA ==========")

    # ==========================================
    # LOAD STUDENT RECORDS
    # ==========================================

    student_records = load_Students_json()
    students = []

    for record in student_records:

        if not validate_student_id(record["student_id"]):
            raise ValueError("Invalid Student ID in JSON file.")

        if not validate_email(record["email"]):
            raise ValueError("Invalid student email in JSON file.")

        # Create each student INSIDE the loop
        student = Student(
            student_id=record["student_id"],
            name=record["name"],
            age=record["age"],
            email=record["email"],
            department=record["department"]
        )

        student.created_at = record.get(
            "created_at", student.created_at
        )
        student.updated_at = record.get(
            "updated_at", student.updated_at
        )

        students.append(student)

    # ==========================================
    # LOAD FACULTY RECORDS
    # ==========================================

    faculty_records = load_faculty_json()
    faculties = []

    for record in faculty_records:

        if not validate_faculty_id(record["faculty_id"]):
            raise ValueError("Invalid Faculty ID in JSON file.")

        if not validate_email(record["email"]):
            raise ValueError("Invalid faculty email in JSON file.")

        # Create each faculty member INSIDE the loop
        faculty_obj = Faculty(
            faculty_id=record["faculty_id"],
            name=record["name"],
            age=record["age"],
            email=record["email"],
            department=record["department"]
        )

        faculty_obj.created_at = record.get(
            "created_at", faculty_obj.created_at
        )
        faculty_obj.updated_at = record.get(
            "updated_at", faculty_obj.updated_at
        )

        faculties.append(faculty_obj)

    # ==========================================
    # LOAD COURSE RECORDS
    # ==========================================

    course_records = load_courses_json()
    courses = []

    for record in course_records:

        if not validate_course_code(record["course_code"]):
            raise ValueError("Invalid Course Code in JSON file.")

        # Create each course INSIDE the loop
        course = Course(
            course_code=record["course_code"],
            course_name=record["course_name"],
            credits=record["credits"]
        )

        course.created_at = record.get(
            "created_at", course.created_at
        )
        course.updated_at = record.get(
            "updated_at", course.updated_at
        )

        courses.append(course)

    # ==========================================
    # CREATE LOOKUP DICTIONARIES
    # ==========================================

    student_lookup = {
        student.student_id: student
        for student in students
    }

    course_lookup = {
        course.course_code: course
        for course in courses
    }

    # ==========================================
    # LOAD ENROLLMENTS
    # ==========================================

    enrollment_records = load_enrollments_json()
    enrollments = []

    for record in enrollment_records:

        student_id = record["student_id"]
        course_code = record["course_code"]

        if student_id not in student_lookup:
            raise ValueError(
                f"Enrollment refers to unknown student: {student_id}"
            )

        if course_code not in course_lookup:
            raise ValueError(
                f"Enrollment refers to unknown course: {course_code}"
            )

        enrollment = Enrollment(
            enrollment_id=record["enrollment_id"],
            student=student_lookup[student_id],
            course=course_lookup[course_code]
        )

        enrollments.append(enrollment)

    # ==========================================
    # RESTORE SERVICE LISTS
    # ==========================================

    student_service.students = students
    faculty_service.faculties = faculties
    course_service.courses = courses
    enrollment_service.enrollments = enrollments

    print("\nStudent IDs loaded:", list(student_lookup.keys()))
    print("Course codes loaded:", list(course_lookup.keys()))

    print("\nAll application data imported successfully!")

    return {
        "students": len(students),
        "faculty": len(faculties),
        "courses": len(courses),
        "enrollments": len(enrollments)
    }

