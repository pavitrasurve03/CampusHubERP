
from abc import ABC, abstractmethod

from app.core.descriptors import Name, Email, Age
from app.core.metaclasses import BaseModel


class Person(BaseModel, ABC):
    """Abstract base class for Student and Faculty."""

    name = Name()
    age = Age()
    email = Email()

    def __init__(self, name, age, email, department):
        self.name = name
        self.age = age
        self.email = email
        self.department = department

    @abstractmethod
    def display_details(self):
        pass

    @abstractmethod
    def to_dict(self):
        pass
