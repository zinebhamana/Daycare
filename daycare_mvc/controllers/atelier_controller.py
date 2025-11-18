from models.atelier import Atelier
from models.JSONStorage import JSONStorage
from controllers.child_controller import list_children
from controllers.employee_controller import list_employees

atelier_storage = JSONStorage("ateliers.json")

def list_ateliers():
    ateliers_data = atelier_storage.load_data()
    ateliers = [Atelier.from_dict(a) for a in ateliers_data]

    all_children = {c.id: c for c in list_children()}
    all_employees = {e.id: e for e in list_employees()}

    for atelier in ateliers:
        atelier.children = [all_children[cid] for cid in atelier.children_ids if cid in all_children]
        atelier.employees = [all_employees[eid] for eid in atelier.employee_ids if eid in all_employees]

    return ateliers


def add_atelier(name, children_ids=None, employee_ids=None):
    """
    Add a new atelier and save to storage
    :param name: Name of the atelier
    :param children_ids: List of child IDs
    :param employee_ids: List of employee IDs
    """
    ateliers = list_ateliers()
    new_id = max([a.id for a in ateliers], default=0) + 1
    new_atelier = Atelier(new_id, name, "2025-11-30", children_ids or [], employee_ids or [])
    ateliers.append(new_atelier)

    atelier_storage.save_data([a.to_dict() for a in ateliers])
    return new_atelier


def get_atelier_by_id(atelier_id):
    """
    Retrieve an atelier by ID
    """
    ateliers = list_ateliers()
    for atelier in ateliers:
        if atelier.id == atelier_id:
            return atelier
    return None


def remove_atelier(atelier_id):
    """
    Remove an atelier by ID
    """
    ateliers = list_ateliers()
    ateliers = [a for a in ateliers if a.id != atelier_id]
    atelier_storage.save_data([a.to_dict() for a in ateliers])


def get_children_names(atelier):
    """
    Convert children IDs to names
    """
    return [child.name for child in atelier.children]


def get_employees_names(atelier):
    """
    Convert employee IDs to names
    """
    return [emp.name for emp in atelier.employees]
