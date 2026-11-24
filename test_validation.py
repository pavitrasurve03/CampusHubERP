#from app.core.validators import (
    #validate_email,
   # validate_student_id,
  #  validate_faculty_id,
 #   validate_course_code
#)

#print("Email:", validate_email("test@gmail.com"))

#print("Student ID:", validate_student_id("ST001"))

#print("Faculty ID:", validate_faculty_id("FC001"))

#print("Course Code:", validate_course_code("CS101"))

#print("Invalid Student ID:", validate_student_id("ST12"))


#from app.database.db import initialize_database
#from app.services.student_service import StudentService
#from app.database.db import initialize_database
#from app.services.faculty_service import FacultyService
#from app.services.course_service import CourseService


# Initialize database
#initialize_database()

# Create services
#student_service = StudentService()
#faculty_service = FacultyService()
#course_service = CourseService()


#print("\n========== WEEK 7 DATABASE TEST ==========")

# Add student
#student = student_service.add_student(
 #   "Test Student",
  #  20,
   ##"Computer Science"
#)

# Add faculty
#faculty = faculty_service.add_faculty(
 #   "Test Faculty",
  #  40,
   # "testfaculty@gmail.com",
    #"Computer Science"
#)

# Add course
#course = course_service.add_course(
 #   "Test Database Course",
  #  4
#)

# Display database records
#student_service.list_students()
#faculty_service.list_faculty()
#course_service.list_courses()

#print("\n========== DATABASE TEST COMPLETED ==========")

# from app.database.db import initialize_database
# from app.services.student_service import StudentService
# from app.services.course_service import CourseService
# from app.services.enrollment_service import EnrollmentService

# # Initialize database
# initialize_database()

# # Create service objects
# student_service = StudentService()
# course_service = CourseService()
# enrollment_service = EnrollmentService()

# print("\n========== ENROLLMENT DATABASE TEST ==========")

# # Get existing students and courses
# students = student_service.students
# courses = course_service.courses

# if not students:
#     print("No students found. Add a student first.")

# elif not courses:
#     print("No courses found. Add a course first.")

# else:
#     # Select the first available student and course
#     student = students[0]
#     course = courses[0]

#     print(f"\nStudent: {student.name} ({student.student_id})")
#     print(f"Course: {course.course_name} ({course.course_code})")

#     # Enroll student
#     enrollment_service.enroll_student(
#     student,
#     course
# )

#     # Display all enrollments
#     enrollment_service.list_enrollments()

# print("\n========== ENROLLMENT TEST COMPLETED ==========")


# import sqlite3

# from app.database.db import initialize_database
# from app.services.enrollment_service import EnrollmentService

# # Initialize database
# initialize_database()

# enrollment_service = EnrollmentService()

# print("\n========== ENROLLMENT DELETE TEST ==========")

# # Display existing enrollments
# print("\nBefore deletion:")
# enrollment_service.list_enrollments()

# # Delete EN001
# print("\nDeleting enrollment EN001...")
# enrollment_service.remove_enrollment("EN001")

# # Display enrollments after deletion
# print("\nAfter deletion:")
# enrollment_service.list_enrollments()

# # Verify directly in SQLite
# connection = sqlite3.connect("campushub.db")

# record = connection.execute(
#     "SELECT * FROM enrollments WHERE enrollment_id = ?",
#     ("EN001",)
# ).fetchone()

# connection.close()

# if record is None:
#     print("\nDatabase verification: EN001 deleted successfully!")
# else:
#     print("\nDatabase verification: Enrollment still exists!")

# print("\n========== TEST COMPLETED ==========")


# from app.database.db import initialize_database
# from app.services.student_service import StudentService
# from app.services.faculty_service import FacultyService
# from app.services.course_service import CourseService

# initialize_database()

# student_service = StudentService()
# faculty_service = FacultyService()
# course_service = CourseService()

# print("\n========== WEEK 7 UPDATE TEST ==========")

# # STUDENT UPDATE
# students = student_service.students

# if students:
#     student = students[0]
#     print("\nUpdating student:", student.student_id)

#     student_service.update_student(
#         student.student_id,
#         department="Information Technology"
#     )

# # FACULTY UPDATE
# faculties = faculty_service.faculties

# if faculties:
#     faculty = faculties[0]
#     print("\nUpdating faculty:", faculty.faculty_id)

#     faculty_service.update_faculty(
#         faculty.faculty_id,
#         department="Computer Science"
#     )

# # COURSE UPDATE
# courses = course_service.courses

# if courses:
#     course = courses[0]
#     print("\nUpdating course:", course.course_code)

#     course_service.update_course(
#         course.course_code,
#         course_name="Updated Database Course"
#     )

# # DISPLAY UPDATED RECORDS
# print("\n========== UPDATED RECORDS ==========")

# student_service.list_students()
# faculty_service.list_faculty()
# course_service.list_courses()

# print("\n========== UPDATE TEST COMPLETED ==========")

# from app.database.db import initialize_database

# from app.services.student_service import StudentService
# from app.services.faculty_service import FacultyService
# from app.services.course_service import CourseService


# initialize_database()

# student_service = StudentService()
# faculty_service = FacultyService()
# course_service = CourseService()

# print("\n========== WEEK 7 DELETE TEST ==========")

# # Delete one student
# students = student_service.students

# if students:
#     student_id = students[-1].student_id
#     print(f"\nDeleting Student: {student_id}")
#     student_service.remove_student(student_id)
# else:
#     print("\nNo students available for deletion.")

# # Delete one faculty member
# faculties = faculty_service.faculties

# if faculties:
#     faculty_id = faculties[-1].faculty_id
#     print(f"\nDeleting Faculty: {faculty_id}")
#     faculty_service.remove_faculty(faculty_id)
# else:
#     print("\nNo faculty available for deletion.")

# # Delete one course
# courses = course_service.courses

# if courses:
#     course_code = courses[-1].course_code
#     print(f"\nDeleting Course: {course_code}")
#     course_service.remove_course(course_code)
# else:
#     print("\nNo courses available for deletion.")

# print("\n========== REMAINING RECORDS ==========")

# student_service.list_students()
# faculty_service.list_faculty()
# course_service.list_courses()

# print("\n========== DELETE TEST COMPLETED ==========")


# from app.database.db import initialize_database
# from app.database.repository import repository

# from app.services.enrollment_service import EnrollmentService

# initialize_database()

# enrollment_service = EnrollmentService()

# print("\n========== RELATIONSHIP TEST ==========")

# # Fetch existing records
# student = repository.get_student("ST001")
# course = repository.get_course("CS001")

# if student is None or course is None:
#     print("Required student or course record not found.")
# else:
#     print("\n1. Creating an enrollment...")

#     enrollment = enrollment_service.enroll_student(
#         student,
#         course
#     )

#     if enrollment is not None:
#         print("\n2. Testing student deletion protection...")

#         student_result = repository.delete_student("ST001")

#         if student_result is False:
#             print("PASS: Student deletion was prevented.")
#         else:
#             print("FAIL: Student was deleted unexpectedly.")

#         print("\n3. Testing course deletion protection...")

#         course_result = repository.delete_course("CS001")

#         if course_result is False:
#             print("PASS: Course deletion was prevented.")
#         else:
#             print("FAIL: Course was deleted unexpectedly.")

#         print("\n4. Removing the test enrollment...")

#         enrollment_service.remove_enrollment(
#             enrollment.enrollment_id
#         )

#         print("\n5. Checking remaining enrollment records...")
#         enrollment_service.list_enrollments()

# print("\n========== TEST COMPLETED ==========")


# from app.utils.logger import log_info, log_error, log_warning

# log_info("Student Added")
# log_info("Student Updated")
# log_info("Faculty Added")
# log_info("Course Added")
# log_info("Enrollment Created")

# log_warning("Student record requires verification")
# log_error("Student not found")

# print("Logging test completed successfully!")


# from app.core.factory import ModelFactory

# student = ModelFactory.create_model(
#     "student",
#     student_id="ST900",
#     name="Factory Student",
#     age=19,
#     email="factory.student@gmail.com",
#     department="Computer Science"
# )

# faculty = ModelFactory.create_model(
#     "faculty",
#     faculty_id="FC900",
#     name="Factory Faculty",
#     age=35,
#     email="factory.faculty@gmail.com",
#     department="Information Technology"
# )

# course = ModelFactory.create_model(
#     "course",
#     course_code="CS900",
#     course_name="Python Programming",
#     credits=4
# )

# print(student.to_dict())
# print(faculty.to_dict())
# print(course.to_dict())

# print("Factory Method working successfully!")

