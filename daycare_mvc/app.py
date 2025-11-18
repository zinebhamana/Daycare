# app.py
import json

from flask import Flask, render_template, request, redirect, url_for
from controllers.child_controller import list_children, add_child
from controllers.employee_controller import list_employees, add_employee
# Correct imports
from controllers.atelier_controller import list_ateliers, add_atelier, get_children_names, get_employees_names

from controllers.abonnement_controller import (
    list_abonnements,
    add_abonnement,
    get_children_names
)

app = Flask(__name__)
employees_list = []  # global in-memory list
with open("employees.json", "r") as f:
    employees_list = json.load(f)
# -------------------- HOME --------------------
@app.route('/')
def home():
    return render_template("index.html")

# -------------------- CHILDREN --------------------
@app.route('/children')
def children():
    children_list = list_children()
    return render_template("children.html", children=children_list)

@app.route('/add_child', methods=['POST'])
def add_new_child():
    name = request.form['name']
    age = int(request.form['age'])
    parent_name = request.form.get('parent_name')
    parent_contact = request.form.get('parent_contact')

    # Call the controller function
    add_child(name, age, parent_name, parent_contact)

    # Redirect back to the children list page
    return redirect(url_for('children'))

@app.route('/delete_child/<int:child_id>', methods=['POST'])
def delete_child(child_id):
    child = Child.query.get(child_id)
    if child:
        db.session.delete(child)
        db.session.commit()
    return redirect(url_for('children'))


# -------------------- EMPLOYEES --------------------
# -------------------- EMPLOYEES --------------------
EMPLOYEES_FILE = 'employees.json'

# Helper functions
def load_employees():
    if os.path.exists(EMPLOYEES_FILE):
        with open(EMPLOYEES_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_employees(employees):
    with open(EMPLOYEES_FILE, 'w', encoding='utf-8') as f:
        json.dump(employees, f, indent=4, ensure_ascii=False)
 # global in-memory list

@app.route('/employees')
def employees():
    return render_template('employees.html', employees=employees_list)


@app.route('/add_employee', methods=['POST'])
def add_new_employee():
    new_id = len(employees_list) + 1
    emp = Employee(
        employee_id=new_id,
        name=request.form['name'],
        role=request.form['role'],
        contact=request.form.get('contact')
    )
    employees_list.append(emp)
    return redirect(url_for('employees'))


@app.route('/delete_employee/<int:employee_id>', methods=['POST'])
def delete_employee(employee_id):
    global employees_list
    employees_list = [e for e in employees_list if e.id != employee_id]
    return redirect(url_for('employees'))

# -------------------- ATELIERS --------------------
@app.route('/ateliers')
def ateliers():
    ateliers_list = list_ateliers()
    children_list = list_children()
    employees_list = list_employees()

    # Prepare dictionaries mapping atelier ID to participant/employee names
    participants_names = {a.id: get_children_names(a) for a in ateliers_list}
    employees_names_dict = {a.id: get_employees_names(a) for a in ateliers_list}

    return render_template(
        "ateliers.html",
        ateliers=ateliers_list,
        children=children_list,
        employees=employees_list,
        participants_names=participants_names,
        employees_names=employees_names_dict
    )

@app.route('/add_atelier', methods=['POST'])
def add_new_atelier():
    name = request.form['name']
    participant_ids = request.form.getlist('participant_ids')
    employee_ids = request.form.getlist('employee_ids')

    # Convert IDs to integers
    participant_ids = [int(pid) for pid in participant_ids]
    employee_ids = [int(eid) for eid in employee_ids]

    add_atelier(name, participant_ids, employee_ids)
    return redirect(url_for('ateliers'))

@app.route('/delete_atelier/<int:atelier_id>', methods=['POST'])
def delete_atelier(atelier_id):
    atelier = Atelier.query.get(atelier_id)
    if atelier:
        db.session.delete(atelier)
        db.session.commit()
    return redirect(url_for('ateliers'))


# -------------------- ABONNEMENTS --------------------
@app.route("/abonnements")
def abonnements():
    abonnements = list_abonnements()   # existing abonnements
    children = list_children()         # list of all children
    return render_template(
        "abonnements.html",
        abonnements=abonnements,
        children=children
    )


@app.route('/add_abonnement', methods=['POST'])
def add_new_abonnement():
    type_name = request.form['type_name']
    price = float(request.form['price'])
    child_ids = request.form.getlist('child_ids')

    # Convert child IDs to integers
    child_ids = [int(cid) for cid in child_ids]

    add_abonnement(type_name, price, child_ids)
    return redirect(url_for('abonnements'))

# -------------------- RUN APP --------------------
if __name__ == "__main__":
    app.run(debug=True)
