
import re


# ==========================================
# EMAIL VALIDATION
# ==========================================

def validate_email(email):

    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    if re.fullmatch(pattern, email):
        return True

    return False


# ==========================================
# STUDENT ID VALIDATION
# ==========================================

def validate_student_id(student_id):

    pattern = r"ST\d{3}"

    return bool(re.fullmatch(pattern, student_id))


# ==========================================
# FACULTY ID VALIDATION
# ==========================================

def validate_faculty_id(faculty_id):

    pattern = r"FC\d{3}"

    return bool(re.fullmatch(pattern, faculty_id))


# ==========================================
# COURSE CODE VALIDATION
# ==========================================

def validate_course_code(course_code):

    pattern = r"CS\d{3}"

    return bool(re.fullmatch(pattern, course_code))
