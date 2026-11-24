
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.services.enrollment_service import EnrollmentService
from app.services.student_service import StudentService
from app.services.course_service import CourseService

router = APIRouter()

enrollment_service = EnrollmentService()
student_service = StudentService()
course_service = CourseService()


class EnrollmentCreate(BaseModel):
    student_id: str = Field(min_length=1)
    course_code: str = Field(min_length=1)


@router.get("/enrollments")
def get_all_enrollments():
    enrollments = enrollment_service.list_enrollments()
    return [enrollment.to_dict() for enrollment in enrollments]


@router.post("/enrollments", status_code=201)
def create_enrollment(data: EnrollmentCreate):

    student = student_service.get_student(data.student_id)

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    course = course_service.get_course(data.course_code)

    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    enrollment = enrollment_service.enroll_student(student, course)

    if enrollment is None:
        raise HTTPException(
            status_code=409,
            detail="Student is already enrolled in this course"
        )

    return enrollment.to_dict()


@router.delete("/enrollments/{enrollment_id}")
def delete_enrollment(enrollment_id: str):

    result = enrollment_service.remove_enrollment(enrollment_id)

    if not result:
        raise HTTPException(status_code=404, detail="Enrollment not found")

    return {"message": "Enrollment deleted successfully"}
