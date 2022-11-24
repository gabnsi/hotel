import sqlite3
fichier_bdd = "bdd.db"
conn = sqlite3.connect(fichier_bdd)
cur = conn.cursor()

req = "INSERT INTO client (nom, prenom) VALUES(?, ?)"

from random import choice

PRENOMS = (
  "Antoine",
  "Amaury",
  "Jean",
  "Martine",
  "Hugo",
  "Gabriel"
  "Baptiste",
  "George"
)

NOMS = (
  "Abad",
  "Boquet",
  "Dupont",
  "Delarue",
  "Hazard",
  "Holland",
  "Brady",
  "Mejda"
)

for i in range(10):
    p = choice(PRENOMS)
    n = choice(NOMS)
    cur.execute(req, (n, p))

conn.commit()

cur.close()
conn.close()