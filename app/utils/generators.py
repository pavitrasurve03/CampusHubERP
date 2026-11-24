
# WEEK 2: ID GENERATORS

def id_generator(prefix):
    counter = 0

    def generate_id():
        nonlocal counter
        counter += 1
        return f"{prefix}{counter:03d}"

    return generate_id


generate_student_id = id_generator("ST")
generate_faculty_id = id_generator("FC")
generate_course_id = id_generator("CS")


# WEEK 3: REPORT GENERATORS

def student_report(students):
    """Yield one student record at a time."""
    for student in students:
        yield student


def faculty_report(faculties):
    """Yield one faculty record at a time."""
    for faculty in faculties:
        yield faculty


def course_report(courses):
    """Yield one course record at a time."""
    for course in courses:
        yield course
