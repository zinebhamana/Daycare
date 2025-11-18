import webbrowser

# ------------------ Classes de base ------------------
class Enfant:
    def __init__(self, id, nom, prenom, groupe):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.groupe = groupe

class Employe:
    def __init__(self, id, nom, prenom, poste):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.poste = poste

# ------------------ Ateliers et EventManager ------------------
class Atelier:
    """Classe de base pour tous les événements"""
    def __init__(self, nom, description, date, duree, animateur=None):
        self.nom = nom
        self.description = description
        self.date = date
        self.duree = duree
        self.animateur = animateur
        self.participants = []

    def ajouter_participant(self, enfant):
        self.participants.append(enfant)

# Sous-classes pour OCP
class Trip(Atelier):
    def __init__(self, nom, description, date, duree, lieu, animateur=None):
        super().__init__(nom, description, date, duree, animateur)
        self.lieu = lieu

class Meeting(Atelier):
    def __init__(self, nom, description, date, duree, sujet, animateur=None):
        super().__init__(nom, description, date, duree, animateur)
        self.sujet = sujet

class Competition(Atelier):
    def __init__(self, nom, description, date, duree, type_competition, animateur=None):
        super().__init__(nom, description, date, duree, animateur)
        self.type_competition = type_competition

class EventManager:
    def __init__(self):
        self.ateliers = []

    def ajouter_atelier(self, atelier):
        self.ateliers.append(atelier)

    def afficher_ateliers(self):
        print("\nListe des événements :")
        for a in self.ateliers:
            animateur = a.animateur.nom if a.animateur else "Aucun"
            info = getattr(a, "lieu", getattr(a, "sujet", getattr(a, "type_competition", "")))
            print(f"{a.nom} ({a.date}, {a.duree}) - Animateur : {animateur} - Info: {info}")
            if a.participants:
                for p in a.participants:
                    print(f"  - {p.nom} {p.prenom}")
            else:
                print("  Aucun participant")

# ------------------ Abonnements et FinanceManager ------------------
class Abonnement:
    """Classe de base pour tous les abonnements"""
    def __init__(self, montant, date):
        self.montant = montant
        self.date = date
        self.etatPaiement = "Non payée"

class Donation(Abonnement):
    def __init__(self, montant, date, donateur=None):
        super().__init__(montant, date)
        self.donateur = donateur

class MonthlySubscription(Abonnement):
    def __init__(self, montant, date, mois):
        super().__init__(montant, date)
        self.mois = mois
        self.type_abonnement = "Mensuel"

class AnnualSubscription(Abonnement):
    def __init__(self, montant, date, annee):
        super().__init__(montant, date)
        self.annee = annee
        self.type_abonnement = "Annuel"

class FinanceManager:
    def __init__(self):
        self.abonnements = []

    def ajouter_abonnement(self, abonnement):
        self.abonnements.append(abonnement)

# ------------------ Garderie ------------------
class Garderie:
    def __init__(self, nom, adresse):
        self.nom = nom
        self.adresse = adresse
        self.enfants = []
        self.employes = []
        self.event_manager = EventManager()
        self.finance_manager = FinanceManager()

    def ajouter_enfant(self, enfant):
        self.enfants.append(enfant)

    def ajouter_employe(self, employe):
        self.employes.append(employe)

    def afficher_enfants(self):
        print("\nListe des enfants :")
        for e in self.enfants:
            print(f"{e.nom} {e.prenom} - Groupe: {e.groupe}")

# ------------------ HTMLManager ------------------
class HTMLManager:
    @staticmethod
    def generer_garderie_html(garderie):
        html = f"<html><head><meta charset='utf-8'><title>{garderie.nom}</title></head><body>"
        html += f"<h1>{garderie.nom} - Garderie</h1>"

        html += "<h2>Enfants</h2><table border='1'><tr><th>Nom</th><th>Prénom</th><th>Groupe</th></tr>"
        for e in garderie.enfants:
            html += f"<tr><td>{e.nom}</td><td>{e.prenom}</td><td>{e.groupe}</td></tr>"
        html += "</table>"

        html += "<h2>Événements</h2>"
        for a in garderie.event_manager.ateliers:
            animateur = a.animateur.nom if a.animateur else "Aucun"
            info = getattr(a, "lieu", getattr(a, "sujet", getattr(a, "type_competition", "")))
            html += f"<h3>{a.nom} ({a.date}, {a.duree}) - Animateur: {animateur} - Info: {info}</h3>"
            if a.participants:
                html += "<ul>"
                for p in a.participants:
                    html += f"<li>{p.nom} {p.prenom} - Groupe: {p.groupe}</li>"
                html += "</ul>"
            else:
                html += "<p>Aucun participant</p>"

        html += "</body></html>"

        with open("../HTML/garderie_ocp.html", "w", encoding="utf-8") as f:
            f.write(html)
        webbrowser.open("../HTML/garderie_ocp.html")
        print("Page HTML générée : garderie_ocp.html")

# ------------------ Exemple d'utilisation ------------------
garderie = Garderie("El yasmine Lilbaraim", "Lakhdaria, Bouira")

# Enfants
e1 = Enfant(1, "Rafaa", "Houda", "Prescolaire")
e2 = Enfant(2, "Nafaa", "Sara", "Bebe")
garderie.ajouter_enfant(e1)
garderie.ajouter_enfant(e2)

# Employés
ens = Employe(1, "Baali", "Hanaa", "Educatrice")
anim = Employe(2, "Djaadi", "Rayane", "Animateur")
garderie.ajouter_employe(ens)
garderie.ajouter_employe(anim)

# Événements
trip = Trip("Sortie zoo", "Visite guidée au zoo", "2025-11-15", "5h", "Zoo de Bouira", animateur=anim)
meeting = Meeting("Réunion parents", "Discussion sur le programme", "2025-11-10", "2h", "Programme annuel", animateur=ens)
competition = Competition("Compétition dessin", "Concours de dessin", "2025-11-20", "3h", "Dessin artistique", animateur=anim)

trip.ajouter_participant(e1)
competition.ajouter_participant(e2)

garderie.event_manager.ajouter_atelier(trip)
garderie.event_manager.ajouter_atelier(meeting)
garderie.event_manager.ajouter_atelier(competition)

# Abonnements
don = Donation(50, "2025-11-04", donateur="Parent Rafaa")
monthly = MonthlySubscription(100, "2025-11-01", "Novembre")
annual = AnnualSubscription(1000, "2025-01-01", 2025)

garderie.finance_manager.ajouter_abonnement(don)
garderie.finance_manager.ajouter_abonnement(monthly)
garderie.finance_manager.ajouter_abonnement(annual)

# Afficher
garderie.afficher_enfants()
garderie.event_manager.afficher_ateliers()

# Générer HTML
HTMLManager.generer_garderie_html(garderie)
