# controllers/employee_controller.py

from models.employee import Employee
from models.JSONStorage import JSONStorage

# Initialize storage for employees
employee_storage = JSONStorage("employees.json")

def list_employees():
    """
    Load all employees and return them as Employee objects
    """
    data = employee_storage.load_data()
    return [Employee.from_dict(item) for item in data]

def add_employee(name, role, contact=None):
    """
    Add a new employee and save to storage
    """
    employees = list_employees()
    new_id = max([emp.id for emp in employees], default=0) + 1
    new_employee = Employee(new_id, name, role, contact)
    employees.append(new_employee)

    # Save all employees back to JSON
    employee_storage.save_data([emp.to_dict() for emp in employees])
    return new_employee

def get_employee_by_id(employee_id):
    """
    Retrieve an employee by ID
    """
    employees = list_employees()
    for emp in employees:
        if emp.id == employee_id:
            return emp
    return None

def remove_employee(employee_id):
    """
    Remove an employee by ID
    """
    employees = list_employees()
    employees = [emp for emp in employees if emp.id != employee_id]
    employee_storage.save_data([emp.to_dict() for emp in employees])
