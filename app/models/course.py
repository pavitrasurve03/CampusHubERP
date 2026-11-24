
from app.core.metaclasses import BaseModel


class Course(BaseModel):

    def __init__(self, course_code, course_name, credits):
        self.course_code = course_code
        self.course_name = course_name
        self.credits = credits

    def display_details(self):
        print("\n--- COURSE DETAILS ---")
        print("Course Code:", self.course_code)
        print("Course Name:", self.course_name)
        print("Credits:", self.credits)
        print("Created At:", self.created_at)
        print("Updated At:", self.updated_at)

    def to_dict(self):
        return {
            "course_code": self.course_code,
            "course_name": self.course_name,
            "credits": self.credits,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
