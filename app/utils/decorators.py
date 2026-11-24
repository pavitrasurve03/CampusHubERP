
import time
from functools import wraps


def log_decorator(func):
    """Prints messages before and after function execution."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\nFunction Started: {func.__name__}")

        try:
            return func(*args, **kwargs)
        finally:
            print(f"Function Completed: {func.__name__}")

    return wrapper


def time_decorator(func):
    """Calculates the execution time of a function."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        try:
            return func(*args, **kwargs)
        finally:
            end_time = time.perf_counter()
            execution_time = end_time - start_time

            print(
                f"Execution Time of {func.__name__}: "
                f"{execution_time:.6f} seconds"
            )

    return wrapper
