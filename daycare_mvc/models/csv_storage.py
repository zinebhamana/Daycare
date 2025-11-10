# daycare_mvc/models/csv_storage.py

import csv
from .storage_interface import StorageInterface  # ← this is correct relative import

class CSVStorage(StorageInterface):
    def __init__(self, filename):
        self.filename = filename

    def load_children(self):
        rows = []
        try:
            with open(self.filename, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for r in reader:
                    # strip fields
                    rows.append({k: v.strip() for k, v in r.items()})
        except FileNotFoundError:
            rows = []
        return rows

    def save_children(self, children_list):
        if not children_list:
            return
        fieldnames = ["ID", "Nom", "Prenom", "Age", "Contact", "Groupe"]
        with open(self.filename, "w", newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for c in children_list:
                writer.writerow(c)
