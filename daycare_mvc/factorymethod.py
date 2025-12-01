# factory_example.py

from abc import ABC, abstractmethod

# Classe abstraite
class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_role(self):
        pass

class Teacher(Employee):
    def get_role(self):
        return "Teacher"

class Cook(Employee):
    def get_role(self):
        return "Cook"

class Cleaner(Employee):
    def get_role(self):
        return "Cleaner"

# Factory Method
class EmployeeFactory:
    @staticmethod
    def create_employee(employee_type, name):
        if employee_type.lower() == "teacher":
            return Teacher(name)
        elif employee_type.lower() == "cook":
            return Cook(name)
        elif employee_type.lower() == "cleaner":
            return Cleaner(name)
        else:
            raise ValueError(f"Unknown employee type: {employee_type}")

# Test Factory
employees = [
    EmployeeFactory.create_employee("Teacher", "Ahmed"),
    EmployeeFactory.create_employee("Cook", "Leila"),
    EmployeeFactory.create_employee("Cleaner", "Mohamed")
]

for e in employees:
    print(f"{e.name} - {e.get_role()}")
