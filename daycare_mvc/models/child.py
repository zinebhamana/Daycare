# models/child.py

class Child:
    def __init__(self, id=None, name=None, age=None, group=None, contact=None):
        self.id = id
        self.name = name
        self.age = age
        self.group = group
        self.contact = contact

    def to_dict(self):
        """Return a dictionary representation of the child."""
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "group": self.group,
            "contact": self.contact
        }

    @staticmethod
    def from_dict(data):
        """Create a Child instance from a dictionary."""
        return Child(
            id=data.get("id"),
            name=data.get("name"),
            age=data.get("age"),
            group=data.get("group"),
            contact=data.get("contact")
        )
