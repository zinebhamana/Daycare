# ------------------ Classe de base et sous-classes ------------------
class Atelier:
    def __init__(self, nom, description, date, duree, animateur=None):
        self.nom = nom
        self.description = description
        self.date = date
        self.duree = duree
        self.animateur = animateur
        self.participants = []

    def ajouter_participant(self, enfant):
        self.participants.append(enfant)

    # Méthode à surcharger par les sous-classes
    def describe(self):
        animateur = self.animateur.nom if self.animateur else "Aucun"
        return f"{self.nom} ({self.date}, {self.duree}) - Animateur: {animateur}"

# Sous-classes
class Trip(Atelier):
    def __init__(self, nom, description, date, duree, lieu, animateur=None):
        super().__init__(nom, description, date, duree, animateur)
        self.lieu = lieu

    def describe(self):
        base = super().describe()
        return f"{base} - Lieu: {self.lieu}"

class Meeting(Atelier):
    def __init__(self, nom, description, date, duree, sujet, animateur=None):
        super().__init__(nom, description, date, duree, animateur)
        self.sujet = sujet

    def describe(self):
        base = super().describe()
        return f"{base} - Sujet: {self.sujet}"

class Competition(Atelier):
    def __init__(self, nom, description, date, duree, type_competition, animateur=None):
        super().__init__(nom, description, date, duree, animateur)
        self.type_competition = type_competition

    def describe(self):
        base = super().describe()
        return f"{base} - Type de compétition: {self.type_competition}"

# ------------------ Fonction LSP ------------------
def display_event_details(event: Atelier):
    """Affiche les détails d'un événement, accepte toutes les sous-classes"""
    print(event.describe())
    if event.participants:
        print("Participants :")
        for p in event.participants:
            print(f"  - {p.nom} {p.prenom}")
    else:
        print("Aucun participant")
    print("-" * 40)

# ------------------ Exemple d'utilisation ------------------
class Enfant:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

class Employe:
    def __init__(self, nom):
        self.nom = nom

# Créer des objets
animateur = Employe("Rayane")
enfant1 = Enfant("Rafaa", "Houda")
enfant2 = Enfant("Nafaa", "Sara")

trip = Trip("Sortie zoo", "Visite guidée au zoo", "2025-11-15", "5h", "Zoo de Bouira", animateur=animateur)
meeting = Meeting("Réunion parents", "Discussion sur le programme", "2025-11-10", "2h", "Programme annuel", animateur=animateur)
competition = Competition("Compétition dessin", "Concours de dessin", "2025-11-20", "3h", "Dessin artistique", animateur=animateur)

trip.ajouter_participant(enfant1)
competition.ajouter_participant(enfant2)

# Afficher détails via LSP
for event in [trip, meeting, competition]:
    display_event_details(event)
