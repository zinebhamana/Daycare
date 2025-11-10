# daycare_mvc/models/entities.py

class Child:
    def __init__(self, id, nom, prenom, age, contact, groupe):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.contact = contact
        self.groupe = groupe

    def to_dict(self):
        return {
            "ID": self.id,
            "Nom": self.nom,
            "Prenom": self.prenom,
            "Age": self.age,
            "Contact": self.contact,
            "Groupe": self.groupe
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=int(data.get("ID", 0)),
            nom=data.get("Nom", ""),
            prenom=data.get("Prenom", ""),
            age=int(data.get("Age", 0)),
            contact=data.get("Contact", ""),
            groupe=data.get("Groupe", "")
        )
