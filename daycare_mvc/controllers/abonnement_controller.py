# controllers/abonnement_controller.py

from models.abonnement import Abonnement
from models.JSONStorage import JSONStorage
from controllers.child_controller import list_children

# Initialize JSON storage
storage = JSONStorage("abonnements.json")


def list_abonnements():
    """
    Load all abonnements from storage and resolve child objects
    """
    data = storage.load_data()
    abonnements = [Abonnement.from_dict(d) for d in data]

    # Map child IDs to Child objects
    all_children = {c.id: c for c in list_children()}

    # Replace children_ids with actual Child objects in .children
    for abo in abonnements:
        abo.children = [all_children[cid] for cid in abo.children_ids if cid in all_children]

    return abonnements


def add_abonnement(type_name, price, child_ids=None):
    """
    Add a new abonnement and save to storage
    :param type_name: Subscription type (e.g., Temps plein)
    :param price: Price of the subscription
    :param child_ids: List of child IDs signed up
    """
    abonnements = list_abonnements()
    new_id = max([a.id for a in abonnements], default=0) + 1
    new_abonnement = Abonnement(new_id, type_name, price, child_ids or [])
    abonnements.append(new_abonnement)

    storage.save_data([a.to_dict() for a in abonnements])
    return new_abonnement


def get_abonnement_by_id(abonnement_id):
    """
    Retrieve an abonnement by ID
    """
    abonnements = list_abonnements()
    for a in abonnements:
        if a.id == abonnement_id:
            return a
    return None


def remove_abonnement(abonnement_id):
    """
    Remove an abonnement by ID
    """
    abonnements = list_abonnements()
    abonnements = [a for a in abonnements if a.id != abonnement_id]
    storage.save_data([a.to_dict() for a in abonnements])


def get_children_names(abonnement):
    """
    Convert child IDs to their names
    :param abonnement: Abonnement object
    :return: List of child names
    """
    return [child.name for child in abonnement.children]
