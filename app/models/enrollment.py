
class Enrollment:

    def __init__(self, enrollment_id, student, course):
        self.enrollment_id = enrollment_id
        self.student = student
        self.course = course

    def display_details(self):

        print("\n--- ENROLLMENT DETAILS ---")
        print("Enrollment ID:", self.enrollment_id)
        print("Student:", self.student.name)
        print("Course:", self.course.course_name)

    def to_dict(self):

        return {
            "enrollment_id": self.enrollment_id,
            "student_id": self.student.student_id,
            "student_name": self.student.name,
            "course_code": self.course.course_code,
            "course_name": self.course.course_name
        }
