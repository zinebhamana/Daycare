# models/json_storage.py
import json
from .storage_interface import StorageInterface

class JSONStorage(StorageInterface):
    def __init__(self, filename):
        self.filename = filename

    def load_children(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if not content:  # fichier vide
                    return []
                data = json.loads(content)
                if isinstance(data, list):
                    return data
                return []
        except FileNotFoundError:
            return []

    def save_children(self, children_list):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(children_list, f, ensure_ascii=False, indent=2)
