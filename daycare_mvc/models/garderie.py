from interfaces.registrable import Registrable

class Garderie(Registrable):
    def __init__(self, nom, storage=None, ui=None):
        self.nom = nom
        self.enfants = []
        self.employes = []
        self.evenements = []
        self.paiements = []
        self.storage = storage
        self.ui = ui

    def register_member(self, member):
        if hasattr(member, 'groupe'):  # Enfant
            self.enfants.append(member)
            print(f"{member.nom} {member.prenom} inscrit à la garderie")
        else:  # Employé
            self.employes.append(member)
            print(f"{member.nom} inscrit comme employé")

    def ajouter_evenement(self, event):
        self.evenements.append(event)

    def ajouter_paiement(self, paiement):
        self.paiements.append(paiement)

    def display(self):
        if self.ui:
            self.ui.display(self)

    def save(self):
        if self.storage:
            self.storage.save(self)
