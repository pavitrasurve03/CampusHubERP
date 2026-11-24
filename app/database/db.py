
from pathlib import Path

from sqlalchemy import create_engine, event
from sqlalchemy.orm import DeclarativeBase, sessionmaker


# ==========================================
# DATABASE LOCATION
# ==========================================

BASE_DIR = Path(__file__).resolve().parents[2]

DB_PATH = BASE_DIR / "campushub.db"

DATABASE_URL = f"sqlite:///{DB_PATH}"


# ==========================================
# BASE CLASS FOR DATABASE MODELS
# ==========================================

class Base(DeclarativeBase):
    pass


# ==========================================
# DATABASE SINGLETON
# ==========================================

class Database:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):

        if getattr(self, "_initialized", False):
            return

        self.engine = create_engine(
            DATABASE_URL,
            connect_args={"check_same_thread": False}
        )

        @event.listens_for(self.engine, "connect")
        def enable_foreign_keys(connection, record):
            cursor = connection.cursor()
            cursor.execute("PRAGMA foreign_keys=ON")
            cursor.close()

        self.SessionLocal = sessionmaker(
            bind=self.engine,
            autoflush=False,
            expire_on_commit=False
        )

        self._initialized = True

    def get_session(self):
        return self.SessionLocal()

    def create_tables(self):

        # Import models before creating tables
        from app.database import models

        Base.metadata.create_all(bind=self.engine)

        print("Database tables created successfully!")


# Create one database manager instance
db = Database()


# ==========================================
# INITIALIZE DATABASE
# ==========================================

def initialize_database():

    db.create_tables()

    print("Database Location:", DB_PATH)
    print("SQLite Database Initialized!")
