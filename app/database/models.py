
from datetime import datetime

from sqlalchemy import (
    String,
    Integer,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.database.db import Base


# ==========================================
# STUDENT TABLE
# ==========================================

class StudentDB(Base):

    __tablename__ = "students"

    student_id: Mapped[str] = mapped_column(
        String(20), primary_key=True
    )

    name: Mapped[str] = mapped_column(String(100), nullable=False)

    age: Mapped[int] = mapped_column(Integer, nullable=False)

    email: Mapped[str] = mapped_column(
        String(100), nullable=False
    )

    department: Mapped[str] = mapped_column(
        String(100), nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    enrollments: Mapped[list["EnrollmentDB"]] = relationship(
        back_populates="student"
    )

    def to_dict(self):

        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "department": self.department,
            "created_at": self.created_at.isoformat()
                if self.created_at else None,
            "updated_at": self.updated_at.isoformat()
                if self.updated_at else None
        }

    def display_details(self):

        print("Student ID :", self.student_id)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Email      :", self.email)
        print("Department :", self.department)


# ==========================================
# FACULTY TABLE
# ==========================================

class FacultyDB(Base):

    __tablename__ = "faculty"

    faculty_id: Mapped[str] = mapped_column(
        String(20), primary_key=True
    )

    name: Mapped[str] = mapped_column(String(100), nullable=False)

    age: Mapped[int] = mapped_column(Integer, nullable=False)

    email: Mapped[str] = mapped_column(
        String(100), nullable=False
    )

    department: Mapped[str] = mapped_column(
        String(100), nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    def to_dict(self):

        return {
            "faculty_id": self.faculty_id,
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "department": self.department,
            "created_at": self.created_at.isoformat()
                if self.created_at else None,
            "updated_at": self.updated_at.isoformat()
                if self.updated_at else None
        }

    def display_details(self):

        print("Faculty ID :", self.faculty_id)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Email      :", self.email)
        print("Department :", self.department)


# ==========================================
# COURSE TABLE
# ==========================================

class CourseDB(Base):

    __tablename__ = "courses"

    course_code: Mapped[str] = mapped_column(
        String(20), primary_key=True
    )

    course_name: Mapped[str] = mapped_column(
        String(100), nullable=False
    )

    credits: Mapped[int] = mapped_column(
        Integer, nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    enrollments: Mapped[list["EnrollmentDB"]] = relationship(
        back_populates="course"
    )

    def to_dict(self):

        return {
            "course_code": self.course_code,
            "course_name": self.course_name,
            "credits": self.credits,
            "created_at": self.created_at.isoformat()
                if self.created_at else None,
            "updated_at": self.updated_at.isoformat()
                if self.updated_at else None
        }

    def display_details(self):

        print("Course Code :", self.course_code)
        print("Course Name :", self.course_name)
        print("Credits     :", self.credits)


# ==========================================
# ENROLLMENT TABLE
# ==========================================

class EnrollmentDB(Base):

    __tablename__ = "enrollments"

    enrollment_id: Mapped[str] = mapped_column(
        String(20), primary_key=True
    )

    student_id: Mapped[str] = mapped_column(
        ForeignKey("students.student_id"),
        nullable=False
    )

    course_code: Mapped[str] = mapped_column(
        ForeignKey("courses.course_code"),
        nullable=False
    )

    student: Mapped["StudentDB"] = relationship(
        back_populates="enrollments"
    )

    course: Mapped["CourseDB"] = relationship(
        back_populates="enrollments"
    )

    def to_dict(self):

        return {
            "enrollment_id": self.enrollment_id,
            "student_id": self.student_id,
            "student_name": self.student.name,
            "course_code": self.course_code,
            "course_name": self.course.course_name
        }

    def display_details(self):

        print("Enrollment ID :", self.enrollment_id)
        print("Student       :", self.student.name)
        print("Course        :", self.course.course_name)
