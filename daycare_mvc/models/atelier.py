from interfaces.organizables import Organizable

class Atelier(Organizable):
    def __init__(self, nom, date):
        self.nom = nom
        self.date = date
        self.participants = []

    def schedule(self):
        print(f"{self.nom} est programmé pour le {self.date}")

    def ajouter_participant(self, enfant):
        self.participants.append(enfant)

    def describe(self):
        return f"Atelier {self.nom} le {self.date}"

class Trip(Atelier):
    def __init__(self, nom, date, lieu):
        super().__init__(nom, date)
        self.lieu = lieu

    def schedule(self):
        print(f"{self.nom} au {self.lieu} est programmé pour le {self.date}")

    def describe(self):
        return f"Trip {self.nom} au {self.lieu} le {self.date}"

class Meeting(Atelier):
    def __init__(self, nom, date, sujet):
        super().__init__(nom, date)
        self.sujet = sujet

    def schedule(self):
        print(f"{self.nom} sur '{self.sujet}' est programmé pour le {self.date}")

    def describe(self):
        return f"Meeting {self.nom} sur '{self.sujet}' le {self.date}"
