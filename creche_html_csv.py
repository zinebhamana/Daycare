import csv

# Nom du fichier CSV
filename = ("enfants"
            ".csv")

# Lecture du fichier CSV et classification par groupe
bebes = []
prescolaires = []
preparatoires = []

with open(filename, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        groupe = row['Groupe'].strip().lower()
        if 'bebe' in groupe:
            bebes.append(row)
        elif 'prescolaire' in groupe:
            prescolaires.append(row)
        elif 'preparatoire' in groupe:
            preparatoires.append(row)

# Génération de la page HTML
html_content = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Gestion de la Garderie</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f8ff; color: #333; }
        h1 { text-align: center; color: #2a5d84; }
        h2 { color: #2a5d84; margin-top: 30px; }
        table { border-collapse: collapse; width: 90%; margin: 0 auto 30px auto; background: white; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        th, td { border: 1px solid #ccc; padding: 8px 12px; text-align: center; }
        th { background-color: #bcd4f6; }
    </style>
</head>
<body>
    <h1>Liste des Enfants de la Garderie</h1>
"""

# Fonction pour générer un tableau HTML à partir d'une liste de dictionnaires
def generate_table(title, data):
    if not data:
        return f"<h2>{title}</h2><p style='text-align:center;'>Aucun enfant dans cette catégorie.</p>"
    table_html = f"<h2>{title}</h2><table><tr><th>ID</th><th>Nom</th><th>Âge</th><th>Contact Parent</th></tr>"
    for child in data:
        table_html += f"<tr><td>{child['ID']}</td><td>{child['Nom']}</td><td>{child['Age']}</td><td>{child['Contact']}</td></tr>"
    table_html += "</table>"
    return table_html

# Ajouter les trois tableaux au HTML
html_content += generate_table("Liste des Bébés", bebes)
html_content += generate_table("Liste des Préscolaires", prescolaires)
html_content += generate_table("Liste des Préparatoires", preparatoires)

# Fin du HTML
html_content += """
</body>
</html>
"""

# Sauvegarde dans un fichier HTML
with open("daycare.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("✅ Fichier 'daycare.html' généré avec succès !")
import webbrowser
webbrowser.open("daycare.html")

