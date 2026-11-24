import asyncio
from app.database.db import initialize_database
from app.utils.serializers import export_data
from app.services.async_service import (
    load_all_data,
    generate_all_reports
)

from app.services.student_service import StudentService
from app.services.faculty_service import FacultyService
from app.services.course_service import CourseService

from app.utils.generators import (
    student_report,
    faculty_report,
    course_report
)

from app.utils.file_manager import ReportWriter
from app.utils.iterators import StudentIterator

import threading
from multiprocessing import Process

from app.services.enrollment_service import EnrollmentService

# ==========================================
# WEEK 4: THREADING REPORT FUNCTIONS
# ==========================================

def generate_student_report_thread(students):

    print("Generating Student Report...")

    with ReportWriter("reports/Students.txt") as report:

        report.write("========== STUDENT REPORT ==========\n\n")

        for student in student_report(students):

            report.write(f"Student ID : {student.student_id}\n")
            report.write(f"Name       : {student.name}\n")
            report.write(f"Age        : {student.age}\n")
            report.write(f"Email      : {student.email}\n")
            report.write(f"Department : {student.department}\n")
            report.write("-----------------------------------\n")


def generate_faculty_report_thread(faculties):

    print("Generating Faculty Report...")

    with ReportWriter("reports/faculty.txt") as report:

        report.write("========== FACULTY REPORT ==========\n\n")

        for faculty in faculty_report(faculties):

            report.write(f"Faculty ID : {faculty.faculty_id}\n")
            report.write(f"Name       : {faculty.name}\n")
            report.write(f"Age        : {faculty.age}\n")
            report.write(f"Email      : {faculty.email}\n")
            report.write(f"Department : {faculty.department}\n")
            report.write("-----------------------------------\n")


def generate_course_report_thread(courses):

    print("Generating Course Report...")

    with ReportWriter("reports/courses.txt") as report:

        report.write("========== COURSE REPORT ==========\n\n")

        for course in course_report(courses):

            report.write(f"Course Code : {course.course_code}\n")
            report.write(f"Course Name : {course.course_name}\n")
            report.write(f"Credits     : {course.credits}\n")
            report.write("-----------------------------------\n")


# ==========================================
# WEEK 4: MULTIPROCESSING SUMMARY
# ==========================================

def calculate_summary(total_students, total_faculty,
                      total_courses, total_enrollments):

    print("\n========== CAMPUSHUB ERP SUMMARY ==========")

    print("Total Students    :", total_students)
    print("Total Faculty     :", total_faculty)
    print("Total Courses     :", total_courses)
    print("Total Enrollments :", total_enrollments)

    print("===========================================")

# ==========================================
# WEEK 5: ASYNCIO EXECUTION
# ==========================================

async def run_week5(
    student_service,
    faculty_service,
    course_service,
    enrollment_service
):

    print("\n========== WEEK 5: ASYNCIO ==========")

    # Load all data asynchronously

    loaded_data = await load_all_data(

        student_service.students,

        faculty_service.faculties,

        course_service.courses,

        enrollment_service.enrollments

    )

    # Store the loaded records

    students, faculties, courses, enrollments = loaded_data

    # Generate all reports asynchronously

    await generate_all_reports(
        students,
        faculties,
        courses
    )

    print("\nWeek 5 Async Operations Completed!")


def main():

    # Initialize SQLite database
    initialize_database()

    # Create service objects
    student_service = StudentService()
    faculty_service = FacultyService()
    course_service = CourseService()
    enrollment_service = EnrollmentService()

    print("\n========== CAMPUSHUB ERP ==========")

    # ==========================================
    # STUDENT MANAGEMENT
    # ==========================================

    print("\n========== STUDENT MANAGEMENT ==========")

    if not student_service.students:
        student_service.add_student(
            "Pavitra Surve", 19,
            "pavitra@gmail.com", "Computer Science"
        )

        student_service.add_student(
            "Rahul Sharma", 20,
            "rahul@gmail.com", "Information Technology"
        )

        student_service.add_student(
            "Priya Patil", 21,
            "priya@gmail.com", "Computer Science"
        )

    student_service.list_students("Computer Science")
    student_service.list_students()

    # ==========================================
    # FACULTY MANAGEMENT
    # ==========================================

    print("\n========== FACULTY MANAGEMENT ==========")

    if not faculty_service.faculties:
        faculty_service.add_faculty(
            "Anita Desai", 40,
            "anita@gmail.com", "Computer Science"
        )

        faculty_service.add_faculty(
            "Suresh Patil", 45,
            "suresh@gmail.com", "Mathematics"
        )

    faculty_service.list_faculty()

    # ==========================================
    # COURSE MANAGEMENT
    # ==========================================

    print("\n========== COURSE MANAGEMENT ==========")

    if not course_service.courses:
        course_service.add_course(
            "Python Programming", 4
        )

        course_service.add_course(
            "Database Management Systems", 3
        )

    course_service.list_courses()

    # ==========================================
    # ENROLLMENT MANAGEMENT
    # ==========================================

    print("\n========== ENROLLMENT MANAGEMENT ==========")

    students = student_service.students
    courses = course_service.courses

    if students and courses:

        student = students[0]
        course = courses[0]

        enrollment_service.enroll_student(
            student,
            course
        )

        enrollment_service.list_enrollments()

    else:
        print("Students or courses are not available.")

    # ==========================================
    # WEEK 4: MULTITHREADING
    # ==========================================

    print("\n========== WEEK 4: THREADING ==========")

    student_thread = threading.Thread(
        target=generate_student_report_thread,
        args=(student_service.students,)
    )

    faculty_thread = threading.Thread(
        target=generate_faculty_report_thread,
        args=(faculty_service.faculties,)
    )

    course_thread = threading.Thread(
        target=generate_course_report_thread,
        args=(course_service.courses,)
    )

    # ==========================================
    # WEEK 4: MULTIPROCESSING
    # ==========================================

    total_students = len(student_service.students)
    total_faculty = len(faculty_service.faculties)
    total_courses = len(course_service.courses)
    total_enrollments = len(enrollment_service.enrollments)

    summary_process = Process(
        target=calculate_summary,
        args=(
            total_students,
            total_faculty,
            total_courses,
            total_enrollments
        )
    )

    summary_process.start()

    student_thread.start()
    faculty_thread.start()
    course_thread.start()

    student_thread.join()
    faculty_thread.join()
    course_thread.join()

    summary_process.join()

    print("\nAll reports generated successfully!")

    # ==========================================
    # WEEK 5: ASYNCIO
    # ==========================================

    print("\n========== WEEK 5: ASYNCIO ==========")

    asyncio.run(
        run_week5(
            student_service,
            faculty_service,
            course_service,
            enrollment_service
        )
    )

    # ==========================================
    # WEEK 6: JSON SERIALIZATION
    # ==========================================

    print("\n========== WEEK 6: JSON SERIALIZATION ==========")

    export_data(
        student_service,
        faculty_service,
        course_service,
        enrollment_service
    )

    print("All records exported to JSON successfully!")

    # ==========================================
    # WEEK 3: CUSTOM ITERATOR
    # ==========================================

    print("\nStudents using Custom Iterator:")

    student_iterator = StudentIterator(
        student_service.students
    )

    for student in student_iterator:
        print(student.student_id, "-", student.name)

    print("\n========== PROJECT EXECUTION COMPLETED ==========")


if __name__ == "__main__":
    main()