# controllers/child_controller.py

from models.child import Child
from models.JSONStorage import JSONStorage

# Initialize storage for children
child_storage = JSONStorage("children.json")

def list_children():
    """
    Load all children and return them as Child objects
    """
    data = child_storage.load_data()
    return [Child.from_dict(item) for item in data]

def add_child(name, age, parent_name=None, parent_contact=None):
    """
    Add a new child and save to storage
    """
    children = list_children()
    new_id = max([child.id for child in children], default=0) + 1
    new_child = Child(new_id, name, age, parent_name, parent_contact)
    children.append(new_child)

    # Save all children back to JSON
    child_storage.save_data([child.to_dict() for child in children])
    return new_child

def get_child_by_id(child_id):
    """
    Retrieve a child by ID
    """
    children = list_children()
    for child in children:
        if child.id == child_id:
            return child
    return None

def remove_child(child_id):
    """
    Remove a child by ID
    """
    children = list_children()
    children = [child for child in children if child.id != child_id]
    child_storage.save_data([child.to_dict() for child in children])
