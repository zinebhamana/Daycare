# models/employee.py

class Employee:
    def __init__(self, employee_id, name, role, contact=None):
        """
        Initialize an Employee object.

        :param employee_id: Unique identifier for the employee
        :param name: Name of the employee
        :param role: Role of the employee (e.g., Teacher, Caretaker)
        :param contact: Optional, contact information
        """
        self.id = employee_id
        self.name = name
        self.role = role
        self.contact = contact

    def to_dict(self):
        """
        Convert the Employee object to a dictionary for JSON storage.
        """
        return {
            "id": self.id,
            "name": self.name,
            "role": self.role,
            "contact": self.contact
        }

    @staticmethod
    def from_dict(data):
        """
        Create an Employee object from a dictionary (used when reading JSON data)
        """
        return Employee(
            employee_id=data.get("id"),
            name=data.get("name"),
            role=data.get("role"),
            contact=data.get("contact")
        )
