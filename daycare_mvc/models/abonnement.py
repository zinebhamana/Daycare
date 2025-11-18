class Abonnement:
    def __init__(self, id, type_, price, children_ids=None):
        self.id = id
        self.type = type_
        self.price = price
        self.children_ids = children_ids or []
        self.children = []

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["type"],   # <-- here
            data["price"],
            data.get("children", [])
        )

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "price": self.price,
            "children": self.children_ids
        }
