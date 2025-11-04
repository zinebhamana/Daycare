import webbrowser

class HTMLManager:
    @staticmethod
    def generer_garderie_html(garderie):
        html = f"<html><head><meta charset='utf-8'><title>{garderie.nom}</title></head><body>"
        html += f"<h1>{garderie.nom} - Garderie</h1>"

        html += "<h2>Enfants</h2><ul>"
        for e in garderie.enfants:
            html += f"<li>{e.nom} {e.prenom} ({e.groupe})</li>"
        html += "</ul>"

        html += "<h2>Événements</h2>"
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

        filename = "garderie.html"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)
        webbrowser.open(filename)
