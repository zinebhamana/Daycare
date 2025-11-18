import csv
import webbrowser

# ------------------ Classes principales ------------------

class Parent:
    def __init__(self, id, nom, prenom, tel, email):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.tel = tel
        self.email = email
        self.enfants = []

    def ajouter_enfant(self, enfant):
        self.enfants.append(enfant)

    def contacter_garderie(self):
        return f"Contact du parent {self.nom} : {self.tel} / {self.email}"

    def payer_facture(self, facture):
        facture.etatPaiement = "Payée"
        return f"Facture {facture.id} payée par {self.nom}"

class Abonnement:
    def __init__(self, montant, date, type_abonnement):
        self.montant = montant
        self.date = date
        self.type = type_abonnement

class Enfant:
    def __init__(self, id, nom, prenom, dateNaissance, allergies, emergencyContact, groupe):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.dateNaissance = dateNaissance
        self.allergies = allergies
        self.emergencyContact = emergencyContact
        self.groupe = groupe
        self.abonnements = []
        self.recommandations = []

    def inscrire(self):
        return f"{self.nom} {self.prenom} est inscrit dans le groupe {self.groupe}"

class Employe:
    def __init__(self, id, nom, prenom, poste, dateEmbauche):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.poste = poste
        self.dateEmbauche = dateEmbauche

    def ajouter_activite(self, atelier):
        atelier.animateur = self

class Atelier:
    def __init__(self, nom, description, date, duree, animateur=None):
        self.nom = nom
        self.description = description
        self.date = date
        self.duree = duree
        self.animateur = animateur  # objet Employe
        self.participants = []      # liste d'objets Enfant

    def ajouter_participant(self, enfant):
        self.participants.append(enfant)

class Garderie:
    def __init__(self, nom, adresse):
        self.nom = nom
        self.adresse = adresse
        self.enfants = []
        self.employes = []
        self.ateliers = []

    def ajouter_enfant(self, enfant):
        self.enfants.append(enfant)

    def ajouter_employe(self, employe):
        self.employes.append(employe)

    def ajouter_atelier(self, atelier):
        self.ateliers.append(atelier)

    def afficher_enfants(self):
        print("\nListe des enfants :")
        for e in self.enfants:
            print(f"{e.nom} {e.prenom} - Groupe: {e.groupe}")

    def afficher_ateliers(self):
        print("\nListe des ateliers :")
        for a in self.ateliers:
            animateur = a.animateur.nom if a.animateur else "Aucun"
            print(f"{a.nom} ({a.date}, {a.duree}) - Animateur : {animateur}")
            if a.participants:
                for p in a.participants:
                    print(f"  - {p.nom} {p.prenom}")
            else:
                print("  Aucun participant")

    def afficher_html(self):
        html = f"<html><head><meta charset='utf-8'><title>{self.nom}</title></head><body>"
        html += f"<h1>{self.nom} - Garderie</h1>"

        # Enfants
        html += "<h2>Enfants</h2><table border='1' style='border-collapse: collapse;'><tr><th>Nom</th><th>Prénom</th><th>Groupe</th></tr>"
        for e in self.enfants:
            html += f"<tr><td>{e.nom}</td><td>{e.prenom}</td><td>{e.groupe}</td></tr>"
        html += "</table>"

        # Ateliers
        html += "<h2>Ateliers</h2>"
        for a in self.ateliers:
            animateur = a.animateur.nom if a.animateur else "Aucun"
            html += f"<h3>{a.nom} ({a.date}, {a.duree}) - Animateur : {animateur}</h3>"
            if a.participants:
                html += "<ul>"
                for p in a.participants:
                    html += f"<li>{p.nom} {p.prenom} - Groupe: {p.groupe}</li>"
                html += "</ul>"
            else:
                html += "<p>Aucun participant</p>"

        html += "</body></html>"
        with open("../garderie_atelier.html", "w", encoding="utf-8") as f:
            f.write(html)
        webbrowser.open("../garderie_atelier.html")
        print("Page HTML générée : garderie_atelier.html")

# ------------------ Exemple d'utilisation ------------------

garderie = Garderie("El yasmine Lilbaraim", "Lakhdaria, Bouira")

# Ajouter enfants
garderie.ajouter_enfant(Enfant(1, "Rafaa", "Houda", "2020-05-01", "Aucune", "0560923569", "Prescolaire"))
garderie.ajouter_enfant(Enfant(2, "Nafaa", "Sara", "2021-03-12", "Aucune", "0779263485", "Bebe"))

# Ajouter employés
enseignante = Employe(1, "Baali", "Hanaa", "Educatrice", "2018-09-01")
garderie.ajouter_employe(enseignante)
animateur = Employe(2, "Djaadi", "Rayane", "Animateur", "2019-01-15")
garderie.ajouter_employe(animateur)

# Créer atelier et ajouter participants
atelier_peinture = Atelier("Peinture", "Atelier créatif peinture", "2025-11-01", "2h", animateur=animateur)
atelier_peinture.ajouter_participant(garderie.enfants[0])
atelier_peinture.ajouter_participant(garderie.enfants[1])
garderie.ajouter_atelier(atelier_peinture)

# Afficher en console
garderie.afficher_enfants()
garderie.afficher_ateliers()

# Générer HTML
garderie.afficher_html()
