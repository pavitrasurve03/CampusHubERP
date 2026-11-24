
import os


class ReportWriter:

    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        # Create the parent folder if it does not exist
        folder = os.path.dirname(self.filename)

        if folder:
            os.makedirs(folder, exist_ok=True)

        # Open the file in write mode
        self.file = open(
            self.filename,
            "w",
            encoding="utf-8"
        )

        print(f"Opened report: {self.filename}")

        return self

    def write(self, text):
        self.file.write(text)

    def __exit__(self, exc_type, exc_value, traceback):
        # Automatically close the file
        if self.file:
            self.file.close()

        print(f"Closed report: {self.filename}")

        # Do not suppress any exceptions
        return False
