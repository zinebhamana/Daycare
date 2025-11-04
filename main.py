from abc import ABC, abstractmethod
import json
import csv
import webbrowser

# ------------------ Interfaces DIP ------------------
class StorageInterface(ABC):
    @abstractmethod
    def save(self, data):
        pass

    @abstractmethod
    def load(self):
        pass

class UIInterface(ABC):
    @abstractmethod
    def display(self, garderie):
        pass

# ------------------ Implémentations Storage ------------------
class JSONStorage(StorageInterface):
    def __init__(self, filename):
        self.filename = filename

    def save(self, data):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, default=str)
        print(f"Données sauvegardées dans {self.filename}")

    def load(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

class CSVStorage(StorageInterface):
    def __init__(self, filename):
        self.filename = filename

    def save(self, data):
        with open(self.filename, "w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            for item in data:
                writer.writerow(item)
        print(f"Données sauvegardées dans {self.filename}")

    def load(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                return list(reader)
        except FileNotFoundError:
            return []

# ------------------ Implémentations UI ------------------
class CLIUI(UIInterface):
    def display(self, garderie):
        print(f"\n=== {garderie.nom} ===")
        print("Enfants :")
        for e in garderie.enfants:
            print(f"  - {e.nom} {e.prenom} ({e.groupe})")
        print("Événements :")
        for ev in garderie.evenements:
            print(f"  - {ev.describe()}")
            for p in ev.participants:
                print(f"    * {p.nom} {p.prenom}")
        print("Paiements :")
        for p in garderie.paiements:
            type_paiement = type(p).__name__
            nom_donateur = f" ({p.donateur})" if hasattr(p, "donateur") else ""
            print(f"  - {type_paiement}{nom_donateur}: {p.montant} - {p.etatPaiement}")

class WebUI(UIInterface):
    def display(self, garderie):
        html = f"<html><head><meta charset='utf-8'><title>{garderie.nom}</title></head><body>"
        html += f"<h1>{garderie.nom} - Garderie</h1>"
        html += "<h2>Enfants</h2><ul>"
        for e in garderie.enfants:
            html += f"<li>{e.nom} {e.prenom} ({e.groupe})</li>"
        html += "</ul><h2>Événements</h2>"
        for ev in garderie.evenements:
            html += f"<h3>{ev.describe()}</h3><ul>"
            for p in ev.participants:
                html += f"<li>{p.nom} {p.prenom}</li>"
            html += "</ul>"
        html += "<h2>Paiements</h2><ul>"
        for p in garderie.paiements:
            type_paiement = type(p).__name__
            nom_donateur = f" ({p.donateur})" if hasattr(p, "donateur") else ""
            html += f"<li>{type_paiement}{nom_donateur}: {p.montant} - {p.etatPaiement}</li>"
        html += "</ul></body></html>"
        filename = "garderie_dip.html"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)
        webbrowser.open(filename)
        print(f"Page Web générée : {filename}")

# ------------------ Classes Métier ------------------
class Enfant:
    def __init__(self, nom, prenom, groupe):
        self.nom = nom
        self.prenom = prenom
        self.groupe = groupe

class Employe:
    def __init__(self, nom):
        self.nom = nom

class Payable:
    def process_payment(self):
        pass

class Abonnement(Payable):
    def __init__(self, montant):
        self.montant = montant
        self.etatPaiement = "Non payée"

    def process_payment(self):
        self.etatPaiement = "Payée"

class Donation(Payable):
    def __init__(self, montant, donateur=None):
        self.montant = montant
        self.donateur = donateur
        self.etatPaiement = "Non payée"

    def process_payment(self):
        self.etatPaiement = "Payée"

class Atelier:
    def __init__(self, nom, date):
        self.nom = nom
        self.date = date
        self.participants = []

    def ajouter_participant(self, enfant):
        self.participants.append(enfant)

    def describe(self):
        return f"{self.nom} ({self.date})"

class Trip(Atelier):
    def __init__(self, nom, date, lieu):
        super().__init__(nom, date)
        self.lieu = lieu

    def describe(self):
        return f"{self.nom} ({self.date}) - Lieu: {self.lieu}"

class Meeting(Atelier):
    def __init__(self, nom, date, sujet):
        super().__init__(nom, date)
        self.sujet = sujet

    def describe(self):
        return f"{self.nom} ({self.date}) - Sujet: {self.sujet}"

class Garderie:
    def __init__(self, nom, storage: StorageInterface, ui: UIInterface):
        self.nom = nom
        self.enfants = []
        self.employes = []
        self.evenements = []
        self.paiements = []
        self.storage = storage
        self.ui = ui

    def register_member(self, member):
        if isinstance(member, Enfant):
            self.enfants.append(member)
        elif isinstance(member, Employe):
            self.employes.append(member)

    def ajouter_evenement(self, ev):
        self.evenements.append(ev)

    def ajouter_paiement(self, p):
        self.paiements.append(p)

    def display(self):
        self.ui.display(self)

    def save(self):
        data = {
            "enfants": [(e.nom, e.prenom, e.groupe) for e in self.enfants],
            "employes": [e.nom for e in self.employes],
            "evenements": [ev.describe() for ev in self.evenements],
            "paiements": [(type(p).__name__, getattr(p,"donateur", ""), p.montant, p.etatPaiement) for p in self.paiements]
        }
        self.storage.save(data)

# ------------------ Exemple d'utilisation ------------------
# Choisir le type de stockage et UI
storage = JSONStorage("garderie.json")  # ou CSVStorage("garderie.csv")
ui = WebUI()  # ou CLIUI()

garderie = Garderie("El yasmine Lilbaraim", storage, ui)

# Inscrire membres
e1 = Enfant("Rafaa", "Houda", "Prescolaire")
e2 = Enfant("Nafaa", "Sara", "Bebe")
garderie.register_member(e1)
garderie.register_member(e2)
garderie.register_member(Employe("Rayane"))

# Événements
trip = Trip("Sortie zoo", "2025-11-15", "Zoo de Bouira")
meeting = Meeting("Réunion parents", "2025-11-10", "Programme annuel")
trip.ajouter_participant(e1)
meeting.ajouter_participant(e2)
garderie.ajouter_evenement(trip)
garderie.ajouter_evenement(meeting)

# Paiements
abonnement = Abonnement(100)
don = Donation(50, donateur="Parent Rafaa")
abonnement.process_payment()
don.process_payment()
garderie.ajouter_paiement(abonnement)
garderie.ajouter_paiement(don)

# Afficher via UI et sauvegarder
garderie.display()
garderie.save()
