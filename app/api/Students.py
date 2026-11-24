
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.services.student_service import StudentService

router = APIRouter()
student_service = StudentService()


class StudentCreate(BaseModel):
    name: str = Field(min_length=1)
    age: int = Field(ge=16, le=80)
    email: str
    department: str = Field(min_length=1)


class StudentUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1)
    age: int | None = Field(default=None, ge=16, le=80)
    email: str | None = None
    department: str | None = Field(default=None, min_length=1)


@router.get("/Students")
def get_all_students():
    students = student_service.list_students()
    return [student.to_dict() for student in students]


@router.get("/Students/{student_id}")
def get_student(student_id: str):
    student = student_service.get_student(student_id)

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return student.to_dict()


@router.post("/Students", status_code=201)
def create_student(data: StudentCreate):
    try:
        student = student_service.add_student(
            name=data.name,
            age=data.age,
            email=data.email,
            department=data.department
        )
        return student.to_dict()

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.put("/Students/{student_id}")
def update_student(student_id: str, data: StudentUpdate):
    updates = data.model_dump(exclude_unset=True)

    if not updates:
        raise HTTPException(
            status_code=400,
            detail="Provide at least one field to update"
        )

    try:
        updated = student_service.update_student(student_id, **updates)

        if updated is None:
            raise HTTPException(status_code=404, detail="Student not found")

        student = student_service.get_student(student_id)
        return student.to_dict()

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.delete("/Students/{student_id}")
def delete_student(student_id: str):
    student = student_service.get_student(student_id)

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    result = student_service.remove_student(student_id)

    if not result:
        raise HTTPException(
            status_code=409,
            detail="Cannot delete student because existing enrollments may be linked"
        )

    return {"message": "Student deleted successfully"}
