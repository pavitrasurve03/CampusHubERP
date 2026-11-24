
from app.core.abc_interfaces import Person


class Student(Person):

    def __init__(self, student_id, name, age, email, department):
        super().__init__(name, age, email, department)
        self.student_id = student_id

    def display_details(self):
        print("\n--- STUDENT DETAILS ---")
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Email:", self.email)
        print("Department:", self.department)
        print("Created At:", self.created_at)
        print("Updated At:", self.updated_at)

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "department": self.department,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
