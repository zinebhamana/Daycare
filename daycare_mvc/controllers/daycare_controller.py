# daycare_mvc/controllers/daycare_controller.py
from daycare_mvc.models.entities import Child  # ← import Child class




class DaycareController:
    def __init__(self, storage):
        """
        storage: implements StorageInterface
        """
        self.storage = storage
        self._children = None  # lazy loaded list of Child objects

    def load_children(self):
        raw = self.storage.load_children()
        self._children = [Child.from_dict(r) for r in raw]
        return self._children

    def get_children(self):
        if self._children is None:
            return self.load_children()
        return self._children

    def get_children_by_group(self, group_name):
        return [c for c in self.get_children() if c.groupe.strip().lower() == group_name.strip().lower()]

    def add_child(self, child: Child):
        children = self.get_children()
        # set id as max+1 if id 0
        if child.id == 0:
            child.id = (max([c.id for c in children]) + 1) if children else 1
        children.append(child)
        # persist
        self.storage.save_children([c.to_dict() for c in children])
        return child

    def delete_child(self, child_id):
        # Load all children from storage as dicts
        children = self.storage.load_children()

        # Keep only children whose ID is not equal to child_id
        children = [c for c in children if int(c["ID"]) != child_id]

        # Save updated list back to storage
        self.storage.save_children(children)

        # Reset cached _children so next get_children() reloads from file
        self._children = None

    def save_all(self):
        if self._children is None:
            return
        self.storage.save_children([c.to_dict() for c in self._children])
