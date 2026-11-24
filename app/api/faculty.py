
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.services.faculty_service import FacultyService

router = APIRouter()
faculty_service = FacultyService()


class FacultyCreate(BaseModel):
    name: str = Field(min_length=1)
    age: int = Field(ge=16, le=80)
    email: str
    department: str = Field(min_length=1)


class FacultyUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1)
    age: int | None = Field(default=None, ge=16, le=80)
    email: str | None = None
    department: str | None = Field(default=None, min_length=1)


@router.get("/faculty")
def get_all_faculty():
    faculties = faculty_service.list_faculty()
    return [faculty.to_dict() for faculty in faculties]


@router.get("/faculty/{faculty_id}")
def get_faculty(faculty_id: str):
    faculty = faculty_service.get_faculty(faculty_id)

    if faculty is None:
        raise HTTPException(status_code=404, detail="Faculty not found")

    return faculty.to_dict()


@router.post("/faculty", status_code=201)
def create_faculty(data: FacultyCreate):
    try:
        faculty = faculty_service.add_faculty(
            name=data.name,
            age=data.age,
            email=data.email,
            department=data.department
        )
        return faculty.to_dict()

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.put("/faculty/{faculty_id}")
def update_faculty(faculty_id: str, data: FacultyUpdate):
    updates = data.model_dump(exclude_unset=True)

    if not updates:
        raise HTTPException(
            status_code=400,
            detail="Provide at least one field to update"
        )

    try:
        updated = faculty_service.update_faculty(faculty_id, **updates)

        if updated is None:
            raise HTTPException(status_code=404, detail="Faculty not found")

        faculty = faculty_service.get_faculty(faculty_id)
        return faculty.to_dict()

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.delete("/faculty/{faculty_id}")
def delete_faculty(faculty_id: str):
    faculty = faculty_service.get_faculty(faculty_id)

    if faculty is None:
        raise HTTPException(status_code=404, detail="Faculty not found")

    result = faculty_service.remove_faculty(faculty_id)

    if not result:
        raise HTTPException(status_code=409, detail="Faculty could not be deleted")

    return {"message": "Faculty deleted successfully"}
