# models/atelier.py

class Atelier:
    def __init__(self, id, name, date, children_ids=None, employee_ids=None):
        self.id = id
        self.name = name
        self.date = date
        self.children_ids = children_ids or []  # list of child IDs
        self.employee_ids = employee_ids or []  # list of employee IDs
        self.children = []   # resolved Child objects
        self.employees = []  # resolved Employee objects

    @staticmethod
    def from_dict(data):
        return Atelier(
            id=data.get("id"),
            name=data.get("name"),
            date=data.get("date"),
            children_ids=data.get("children", []),  # matches JSON key
            employee_ids=data.get("employees", [])
        )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "date": self.date,
            "children": self.children_ids,
            "employees": self.employee_ids
        }
