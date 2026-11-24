
from sqlalchemy.orm import joinedload

from app.database.db import db
from app.database.models import (
    StudentDB,
    FacultyDB,
    CourseDB,
    EnrollmentDB
)

from app.models.student import Student
from app.models.faculty import Faculty
from app.models.course import Course
from app.models.enrollment import Enrollment


class Repository:

    # ==========================================
    # STUDENT OPERATIONS
    # ==========================================

    def add_student(self, student):

        session = db.get_session()

        try:
            record = StudentDB(
                student_id=student.student_id,
                name=student.name,
                age=student.age,
                email=student.email,
                department=student.department,
                created_at=student.created_at,
                updated_at=student.updated_at
            )

            session.add(record)
            session.commit()

            return student

        except Exception:
            session.rollback()
            raise

        finally:
            session.close()

    def get_students(self):

        session = db.get_session()

        try:
            records = session.query(StudentDB).all()

            return [
                Student(
                    student_id=r.student_id,
                    name=r.name,
                    age=r.age,
                    email=r.email,
                    department=r.department
                )
                for r in records
            ]

        finally:
            session.close()

    def get_student(self, student_id):

        session = db.get_session()

        try:
            r = session.get(StudentDB, student_id)

            if r is None:
                return None

            return Student(
                student_id=r.student_id,
                name=r.name,
                age=r.age,
                email=r.email,
                department=r.department
            )

        finally:
            session.close()

    def update_student(self, student_id, **kwargs):

        session = db.get_session()

        try:
            record = session.get(StudentDB, student_id)

            if record is None:
                return None

            for key, value in kwargs.items():
                setattr(record, key, value)

            session.commit()

            return self.get_student(student_id)

        except Exception:
            session.rollback()
            raise

        finally:
            session.close()

    def delete_student(self, student_id):

        session = db.get_session()

        try:
            record = session.get(StudentDB, student_id)

            if record is None:
                return False

            session.delete(record)
            
            if session.query(EnrollmentDB).filter_by(
                student_id=student_id
            ).first():
                print("Cannot delete student: Existing enrollments found.")
                return False
            
            session.commit()

            return True

        except Exception:
            session.rollback()
            raise

        finally:
            session.close()

    # ==========================================
    # FACULTY OPERATIONS
    # ==========================================

    def add_faculty(self, faculty):

        session = db.get_session()

        try:
            record = FacultyDB(
                faculty_id=faculty.faculty_id,
                name=faculty.name,
                age=faculty.age,
                email=faculty.email,
                department=faculty.department,
                created_at=faculty.created_at,
                updated_at=faculty.updated_at
            )

            session.add(record)
            session.commit()

            return faculty

        except Exception:
            session.rollback()
            raise

        finally:
            session.close()

    def get_faculty(self):

        session = db.get_session()

        try:
            records = session.query(FacultyDB).all()

            return [
                Faculty(
                    faculty_id=r.faculty_id,
                    name=r.name,
                    age=r.age,
                    email=r.email,
                    department=r.department
                )
                for r in records
            ]

        finally:
            session.close()

    def get_faculty_by_id(self, faculty_id):

        session = db.get_session()

        try:
            r = session.get(FacultyDB, faculty_id)

            if r is None:
                return None

            return Faculty(
                faculty_id=r.faculty_id,
                name=r.name,
                age=r.age,
                email=r.email,
                department=r.department
            )

        finally:
            session.close()

    def update_faculty(self, faculty_id, **kwargs):

        session = db.get_session()

        try:
            record = session.get(FacultyDB, faculty_id)

            if record is None:
                return None

            for key, value in kwargs.items():
                setattr(record, key, value)

            session.commit()

            return self.get_faculty_by_id(faculty_id)

        except Exception:
            session.rollback()
            raise

        finally:
            session.close()

    def delete_faculty(self, faculty_id):

        session = db.get_session()

        try:
            record = session.get(FacultyDB, faculty_id)

            if record is None:
                return False

            session.delete(record)
            session.commit()

            return True

        except Exception:
            session.rollback()
            raise

        finally:
            session.close()

    # ==========================================
    # COURSE OPERATIONS
    # ==========================================

    def add_course(self, course):

        session = db.get_session()

        try:
            record = CourseDB(
                course_code=course.course_code,
                course_name=course.course_name,
                credits=course.credits,
                created_at=course.created_at,
                updated_at=course.updated_at
            )

            session.add(record)
            session.commit()

            return course

        except Exception:
            session.rollback()
            raise

        finally:
            session.close()

    def get_courses(self):

        session = db.get_session()

        try:
            records = session.query(CourseDB).all()

            return [
                Course(
                    course_code=r.course_code,
                    course_name=r.course_name,
                    credits=r.credits
                )
                for r in records
            ]

        finally:
            session.close()

    def get_course(self, course_code):

        session = db.get_session()

        try:
            r = session.get(CourseDB, course_code)

            if r is None:
                return None

            return Course(
                course_code=r.course_code,
                course_name=r.course_name,
                credits=r.credits
            )

        finally:
            session.close()

    def update_course(self, course_code, **kwargs):

        session = db.get_session()

        try:
            record = session.get(CourseDB, course_code)

            if record is None:
                return None

            for key, value in kwargs.items():
                setattr(record, key, value)

            session.commit()

            return self.get_course(course_code)

        except Exception:
            session.rollback()
            raise

        finally:
            session.close()

    def delete_course(self, course_code):

        session = db.get_session()

        try:
            record = session.get(CourseDB, course_code)

            if record is None:
                return False

            session.delete(record)
            
            if session.query(EnrollmentDB).filter_by(
                course_code=course_code
            ).first():
                print("Cannot delete course: Existing enrollments found.")
                return False
            
            session.commit()

            return True

        except Exception:
            session.rollback()
            raise

        finally:
            session.close()

    # ==========================================
    # ENROLLMENT OPERATIONS
    # ==========================================

    def add_enrollment(self, enrollment):

        session = db.get_session()

        try:
            record = EnrollmentDB(
                enrollment_id=enrollment.enrollment_id,
                student_id=enrollment.student.student_id,
                course_code=enrollment.course.course_code
            )

            session.add(record)
            session.commit()

            return enrollment

        except Exception:
            session.rollback()
            raise

        finally:
            session.close()

    def get_enrollments(self):

        session = db.get_session()

        try:
            records = (
                session.query(EnrollmentDB)
                .options(
                    joinedload(EnrollmentDB.student),
                    joinedload(EnrollmentDB.course)
                )
                .all()
            )

            result = []

            for r in records:

                student = Student(
                    student_id=r.student.student_id,
                    name=r.student.name,
                    age=r.student.age,
                    email=r.student.email,
                    department=r.student.department
                )

                course = Course(
                    course_code=r.course.course_code,
                    course_name=r.course.course_name,
                    credits=r.course.credits
                )

                result.append(
                    Enrollment(
                        r.enrollment_id,
                        student,
                        course
                    )
                )

            return result

        finally:
            session.close()

    def get_enrollment(self, enrollment_id):

        session = db.get_session()

        try:
            r = (
                session.query(EnrollmentDB)
                .options(
                    joinedload(EnrollmentDB.student),
                    joinedload(EnrollmentDB.course)
                )
                .filter_by(enrollment_id=enrollment_id)
                .first()
            )

            if r is None:
                return None

            student = Student(
                student_id=r.student.student_id,
                name=r.student.name,
                age=r.student.age,
                email=r.student.email,
                department=r.student.department
            )

            course = Course(
                course_code=r.course.course_code,
                course_name=r.course.course_name,
                credits=r.course.credits
            )

            return Enrollment(
                r.enrollment_id,
                student,
                course
            )

        finally:
            session.close()

    def delete_enrollment(self, enrollment_id):

        session = db.get_session()

        try:
            record = session.get(EnrollmentDB, enrollment_id)

            if record is None:
                return False

            session.delete(record)
            session.commit()

            return True

        except Exception:
            session.rollback()
            raise

        finally:
            session.close()


# Shared repository instance
repository = Repository()
