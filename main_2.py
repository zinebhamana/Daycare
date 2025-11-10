import os
from flask import Flask, render_template, request, redirect, url_for
from daycare_mvc.models.json_storage import JSONStorage
from daycare_mvc.controllers.daycare_controller import DaycareController
from daycare_mvc.models.entities import Child

# --- Flask app with absolute template path ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "daycare_mvc", "templates")
app = Flask(__name__, template_folder=TEMPLATE_DIR)

# --- Storage selection ---
STORAGE_FILE = os.path.join(BASE_DIR, "data", "children.json")
storage = JSONStorage(STORAGE_FILE)

# --- Controller ---
controller = DaycareController(storage)

# --- Routes ---
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/children", methods=["GET", "POST"])
def children():
    if request.method == "POST":
        # créer un enfant depuis le formulaire
        data = {
            "ID": int(request.form.get("id", "0") or 0),
            "Nom": request.form.get("nom", "").strip(),
            "Prenom": request.form.get("prenom", "").strip(),
            "Age": int(request.form.get("age", "0") or 0),
            "Contact": request.form.get("contact", "").strip(),
            "Groupe": request.form.get("groupe", "").strip()
        }
        child = Child.from_dict(data)
        controller.add_child(child)
        return redirect(url_for("children"))

    # filtrer par groupe si demandé
    group = request.args.get("group")
    if group:
        children_list = controller.get_children_by_group(group)
    else:
        children_list = controller.get_children()
    return render_template("children.html", children=children_list, group=group)

@app.route("/delete_child/<int:child_id>", methods=["POST"])
def delete_child(child_id):
    controller.delete_child(child_id)
    return redirect(request.referrer or url_for("children"))

# --- Run server ---
if __name__ == "__main__":
    app.run(debug=True)
