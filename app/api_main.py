
from fastapi import FastAPI

from app.api import Students
from app.api import faculty
from app.api import courses
from app.api import enrollments

from app.database.db import initialize_database

# Initialize the existing SQLite database
initialize_database()

# Create FastAPI application
app = FastAPI(
    title="CampusHub ERP API",
    description="REST API for College Management System",
    version="1.0.0"
)

# Register API routes
app.include_router(Students.router)
app.include_router(faculty.router)
app.include_router(courses.router)
app.include_router(enrollments.router)


@app.get("/")
def home():
    return {
        "message": "Welcome to CampusHub ERP REST API",
        "status": "Running successfully"
    }
