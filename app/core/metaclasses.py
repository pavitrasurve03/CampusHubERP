
from datetime import datetime
from abc import ABCMeta


class ModelMeta(ABCMeta):
    """Metaclass that automatically manages timestamps."""

    def __new__(mcs, name, bases, namespace):

        # Add class-level timestamps
        timestamp = datetime.now()

        namespace.setdefault("created_at", timestamp)
        namespace.setdefault("updated_at", timestamp)

        return super().__new__(mcs, name, bases, namespace)

    def __call__(cls, *args, **kwargs):

        # Create the object
        instance = super().__call__(*args, **kwargs)

        # Add individual object timestamps
        now = datetime.now()
        instance.created_at = now
        instance.updated_at = now

        return instance


class BaseModel(metaclass=ModelMeta):
    """Base class for all application models."""

    def touch(self):
        """Update the modification timestamp."""
        self.updated_at = datetime.now()
