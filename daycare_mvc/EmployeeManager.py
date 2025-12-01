# singleton_example.py

class Employee:
    def __init__(self, employee_id, name, role):
        self.id = employee_id
        self.name = name
        self.role = role

    def __str__(self):
        return f"{self.id} - {self.name} ({self.role})"


class EmployeeManager:
    _instance = None  # Attribut unique pour le Singleton

    def __new__(cls):
        if cls._instance is None:
            print("Création de l'instance EmployeeManager...")
            cls._instance = super(EmployeeManager, cls).__new__(cls)
            cls._instance.employees = []
        return cls._instance

    def add_employee(self, employee):
        self.employees.append(employee)

    def list_employees(self):
        return self.employees


# Test Singleton
manager1 = EmployeeManager()
manager2 = EmployeeManager()

manager1.add_employee(Employee(1, "Ahmed", "Teacher"))
manager2.add_employee(Employee(2, "Sofia", "Cook"))

# Les deux managers pointent vers la même instance
print("Liste des employés via manager1:")
for e in manager1.list_employees():
    print(e)

print("Liste des employés via manager2:")
for e in manager2.list_employees():
    print(e)

print(f"manager1 is manager2 ? {manager1 is manager2}")
