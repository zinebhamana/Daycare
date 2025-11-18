# models/JSONStorage.py

import json
from pathlib import Path

class JSONStorage:
    """
    Simple JSON file storage class for storing lists of dictionaries.
    Can be used for children.json, employees.json, ateliers.json, etc.
    """
    def __init__(self, filename):
        """
        Initialize the storage with a JSON file path.

        :param filename: Path to JSON file
        """
        self.filename = Path(filename)
        if not self.filename.exists():
            # Create empty JSON array if file does not exist
            self.filename.write_text("[]", encoding="utf-8")

    def load_data(self):
        """
        Load the JSON data as a list of dictionaries.
        Returns an empty list if the file is empty or invalid.
        """
        try:
            with self.filename.open("r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save_data(self, data):
        """
        Save a list of dictionaries to the JSON file.

        :param data: List of dictionaries
        """
        with self.filename.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
