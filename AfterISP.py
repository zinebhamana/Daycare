import webbrowser
from abc import ABC, abstractmethod

# ------------------ Interfaces ISP ------------------
class Payable(ABC):
    @abstractmethod
    def process_payment(self):
        pass

class Organizable(ABC):
    @abstractmethod
    def schedule(self):
        pass

class Registrable(ABC):
    @abstractmethod
    def register_member(self, member):
        pass

# ------------------ Classes de base ------------------
class Enfant:
    def __init__(self, nom, prenom, groupe):
        self.nom = nom
        self.prenom = prenom
        self.groupe = groupe

class Employe:
    def __init__(self, nom):
        self.nom = nom

# ------------------ Abonnements Payables ------------------
class Abonnement(Payable):
    def __init__(self, montant):
        self.montant = montant
        self.etatPaiement = "Non payée"

    def process_payment(self):
        self.etatPaiement = "Payée"
        print(f"Paiement de {self.montant} effectué")

class Donation(Payable):
    def __init__(self, montant, donateur=None):
        self.montant = montant
        self.donateur = donateur
        self.etatPaiement = "Non payée"

    def process_payment(self):
        self.etatPaiement = "Payée"
        print(f"Donation de {self.montant} de {self.donateur} reçue")

# ------------------ Événements Organisables ------------------
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
        return f"{self.nom} ({self.date})"

class Trip(Atelier):
    def __init__(self, nom, date, lieu):
        super().__init__(nom, date)
        self.lieu = lieu

    def schedule(self):
        print(f"{self.nom} au {self.lieu} est programmé pour le {self.date}")

    def describe(self):
        return f"{self.nom} ({self.date}) - Lieu: {self.lieu}"

class Meeting(Atelier):
    def __init__(self, nom, date, sujet):
        super().__init__(nom, date)
        self.sujet = sujet

    def schedule(self):
        print(f"{self.nom} sur '{self.sujet}' est programmé pour le {self.date}")

    def describe(self):
        return f"{self.nom} ({self.date}) - Sujet: {self.sujet}"

# ------------------ Garderie Registrable ------------------
class Garderie(Registrable):
    def __init__(self, nom):
        self.nom = nom
        self.enfants = []
        self.employes = []
        self.evenements = []
        self.paiements = []

    def register_member(self, member):
        if isinstance(member, Enfant):
            self.enfants.append(member)
            print(f"{member.nom} {member.prenom} inscrit à la garderie")
        elif isinstance(member, Employe):
            self.employes.append(member)
            print(f"{member.nom} inscrit comme employé")

    def ajouter_evenement(self, evenement):
        self.evenements.append(evenement)

    def ajouter_paiement(self, paiement):
        self.paiements.append(paiement)

# ------------------ HTML Manager ------------------
class HTMLManager:
    @staticmethod
    def generer_garderie_html(garderie):
        html = f"<html><head><meta charset='utf-8'><title>{garderie.nom}</title></head><body>"
        html += f"<h1>{garderie.nom} - Garderie</h1>"

        # Enfants
        html += "<h2>Enfants</h2><table border='1'><tr><th>Nom</th><th>Prénom</th><th>Groupe</th></tr>"
        for e in garderie.enfants:
            html += f"<tr><td>{e.nom}</td><td>{e.prenom}</td><td>{e.groupe}</td></tr>"
        html += "</table>"

        # Événements
        html += "<h2>Événements</h2>"
        for ev in garderie.evenements:
            html += f"<h3>{ev.describe()}</h3>"
            if ev.participants:
                html += "<ul>"
                for p in ev.participants:
                    html += f"<li>{p.nom} {p.prenom} - Groupe: {p.groupe}</li>"
                html += "</ul>"
            else:
                html += "<p>Aucun participant</p>"

        # Paiements
        html += "<h2>Paiements</h2><table border='1'><tr><th>Type</th><th>Montant</th><th>État</th></tr>"
        for p in garderie.paiements:
            type_paiement = type(p).__name__
            nom_donateur = f" ({p.donateur})" if isinstance(p, Donation) else ""
            html += f"<tr><td>{type_paiement}{nom_donateur}</td><td>{p.montant}</td><td>{p.etatPaiement}</td></tr>"
        html += "</table>"

        html += "</body></html>"

        with open("garderie_complete.html", "w", encoding="utf-8") as f:
            f.write(html)
        webbrowser.open("garderie_complete.html")
        print("Page HTML générée : garderie_complete.html")

# ------------------ Exemple d'utilisation ------------------
garderie = Garderie("El yasmine Lilbaraim")

# Inscrire membres
e1 = Enfant("Rafaa", "Houda", "Prescolaire")
e2 = Enfant("Nafaa", "Sara", "Bebe")
garderie.register_member(e1)
garderie.register_member(e2)

emp = Employe("Rayane")
garderie.register_member(emp)

# Événements
trip = Trip("Sortie zoo", "2025-11-15", "Zoo de Bouira")
meeting = Meeting("Réunion parents", "2025-11-10", "Programme annuel")

trip.ajouter_participant(e1)
meeting.ajouter_participant(e2)

garderie.ajouter_evenement(trip)
garderie.ajouter_evenement(meeting)

# Programmer événements
trip.schedule()
meeting.schedule()

# Paiements
abonnement = Abonnement(100)
don = Donation(50, donateur="Parent Rafaa")

abonnement.process_payment()
don.process_payment()

garderie.ajouter_paiement(abonnement)
garderie.ajouter_paiement(don)

# Générer HTML complet
HTMLManager.generer_garderie_html(garderie)
