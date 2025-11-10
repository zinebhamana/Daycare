# models/mysql_storage.py
# OPTIONAL: requires pymysql and a MySQL DB. This is a minimal example.
import pymysql
from .storage_interface import StorageInterface

class MySQLStorage(StorageInterface):
    def __init__(self, host, user, password, db, table="children"):
        self.conn_args = dict(host=host, user=user, password=password, db=db, charset='utf8mb4')
        self.table = table

    def _get_conn(self):
        return pymysql.connect(**self.conn_args)

    def load_children(self):
        rows = []
        conn = self._get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute(f"SELECT id, nom, prenom, age, contact, groupe FROM {self.table}")
                for r in cur.fetchall():
                    rows.append({"ID": r[0], "Nom": r[1], "Prenom": r[2], "Age": r[3], "Contact": r[4], "Groupe": r[5]})
        finally:
            conn.close()
        return rows

    def save_children(self, children_list):
        conn = self._get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute(f"TRUNCATE TABLE {self.table}")  # simple: wipe and insert
                for c in children_list:
                    cur.execute(f"INSERT INTO {self.table} (id, nom, prenom, age, contact, groupe) VALUES (%s,%s,%s,%s,%s,%s)",
                                (c["ID"], c["Nom"], c["Prenom"], c["Age"], c["Contact"], c["Groupe"]))
            conn.commit()
        finally:
            conn.close()
