
# CampusHub ERP – College Management System

## 1. Project Overview

CampusHub ERP is a Python-based College Management System developed to manage student, faculty, course and enrollment information.

The project uses Object-Oriented Programming, functional programming, multithreading, multiprocessing, asynchronous programming, JSON serialization, SQLite and REST APIs.

## 2. Technologies Used

- Python
- SQLite
- SQLAlchemy ORM
- FastAPI
- Uvicorn
- Pydantic
- Pytest

## 3. Main Modules

1. Student Management
2. Faculty Management
3. Course Management
4. Enrollment Management

## 4. Design Patterns

- Singleton Pattern – Database instance management.
- Factory Method Pattern – Model object creation.
- Repository Pattern – Database CRUD operations.

## 5. Project Features

- Add, view, update and delete records.
- Student and faculty validation.
- Course and enrollment management.
- SQLite database persistence.
- JSON data export and import.
- Report generation.
- Multithreading and multiprocessing.
- Asynchronous data loading.
- REST API using FastAPI.
- Application logging.
- Unit testing using Pytest.

## 6. Installation

Clone or download the project.

Install dependencies:

    pip install -r requirements.txt

## 7. Run the Console Application

    python -m app.main

## 8. Run the REST API

    python -m uvicorn app.api_main:app --reload

Open the API documentation:

    http://127.0.0.1:8000/docs

## 9. Run Unit Tests

    python -m pytest tests -v

## 10. Database

The project uses SQLite.

Database file:

    campushub.db

## 11. Project Deliverables

- Complete Python source code.
- SQLite database.
- JSON data files.
- Generated reports.
- Application log file.
- Unit test files.
- Project documentation.
