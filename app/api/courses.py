
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.services.course_service import CourseService

router = APIRouter()
course_service = CourseService()


class CourseCreate(BaseModel):
    course_name: str = Field(min_length=1)
    credits: int = Field(gt=0)


class CourseUpdate(BaseModel):
    course_name: str | None = Field(default=None, min_length=1)
    credits: int | None = Field(default=None, gt=0)


@router.get("/courses")
def get_all_courses():
    courses = course_service.list_courses()
    return [course.to_dict() for course in courses]


@router.get("/courses/{course_code}")
def get_course(course_code: str):
    course = course_service.get_course(course_code)

    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    return course.to_dict()


@router.post("/courses", status_code=201)
def create_course(data: CourseCreate):
    try:
        course = course_service.add_course(
            course_name=data.course_name,
            credits=data.credits
        )
        return course.to_dict()

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.put("/courses/{course_code}")
def update_course(course_code: str, data: CourseUpdate):
    updates = data.model_dump(exclude_unset=True)

    if not updates:
        raise HTTPException(
            status_code=400,
            detail="Provide at least one field to update"
        )

    try:
        updated = course_service.update_course(course_code, **updates)

        if updated is None:
            raise HTTPException(status_code=404, detail="Course not found")

        course = course_service.get_course(course_code)
        return course.to_dict()

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.delete("/courses/{course_code}")
def delete_course(course_code: str):
    course = course_service.get_course(course_code)

    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    result = course_service.remove_course(course_code)

    if not result:
        raise HTTPException(
            status_code=409,
            detail="Cannot delete course because existing enrollments may be linked"
        )

    return {"message": "Course deleted successfully"}
