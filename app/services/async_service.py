
import asyncio
from app.utils.logger import log_info, log_error
from app.utils.generators import (
    student_report,
    faculty_report,
    course_report
)

from app.utils.file_manager import ReportWriter

# ==========================================
# STEP 1: ASYNCHRONOUS DATA LOADING
# ==========================================

async def load_Students(records=None):

    print("Loading Students...")

    await asyncio.sleep(1)

    return records if records is not None else []

async def load_faculty(records=None):

    print("Loading Faculty...")

    await asyncio.sleep(1)

    return records if records is not None else []

async def load_courses(records=None):

    print("Loading Courses...")

    await asyncio.sleep(1)

    return records if records is not None else []

async def load_enrollments(records=None):

    print("Loading Enrollments...")

    await asyncio.sleep(1)

    return records if records is not None else []

# ==========================================
# STEP 2: LOAD ALL DATA TOGETHER
# ==========================================

async def load_all_data(
    students,
    faculties,
    courses,
    enrollments
):

    results = await asyncio.gather(

        load_Students(students),

        load_faculty(faculties),

        load_courses(courses),

        load_enrollments(enrollments)

    )

    print("\nAll data loaded successfully.")

    return results

# ==========================================
# STEP 3: ASYNCHRONOUS REPORT GENERATION
# ==========================================

async def generate_student_report(students):

    await asyncio.sleep(1)

    with ReportWriter("reports/Students.txt") as report:

        report.write("========== STUDENT REPORT ==========\n\n")

        for student in student_report(students):

            report.write(f"Student ID : {student.student_id}\n")
            report.write(f"Name       : {student.name}\n")
            report.write(f"Age        : {student.age}\n")
            report.write(f"Email      : {student.email}\n")
            report.write(f"Department : {student.department}\n")
            report.write("-----------------------------------\n")

    print("Student Report Completed")

async def generate_faculty_report(faculties):

    await asyncio.sleep(1)

    with ReportWriter("reports/faculty.txt") as report:

        report.write("========== FACULTY REPORT ==========\n\n")

        for faculty in faculty_report(faculties):

            report.write(f"Faculty ID : {faculty.faculty_id}\n")
            report.write(f"Name       : {faculty.name}\n")
            report.write(f"Age        : {faculty.age}\n")
            report.write(f"Email      : {faculty.email}\n")
            report.write(f"Department : {faculty.department}\n")
            report.write("-----------------------------------\n")

    print("Faculty Report Completed")

async def generate_course_report(courses):

    await asyncio.sleep(1)

    with ReportWriter("reports/courses.txt") as report:

        report.write("========== COURSE REPORT ==========\n\n")

        for course in course_report(courses):

            report.write(f"Course Code : {course.course_code}\n")
            report.write(f"Course Name : {course.course_name}\n")
            report.write(f"Credits     : {course.credits}\n")
            report.write("-----------------------------------\n")

    print("Course Report Completed")

# ==========================================
# RUN ALL REPORTS TOGETHER
# ==========================================

async def generate_all_reports(students, faculties, courses):

    print("\nGenerating Reports...")

    await asyncio.gather(

        generate_student_report(students),

        generate_faculty_report(faculties),

        generate_course_report(courses)

    )

    print("\nAll Reports Generated Successfully.")