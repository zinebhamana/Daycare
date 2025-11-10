# daycare_mvc/models/storage_interface.py

class StorageInterface:
    def load_children(self):
        raise NotImplementedError

    def save_children(self, children_list):
        raise NotImplementedError
