import sqlite3
fichier_bdd = "bdd.db"
conn = sqlite3.connect(fichier_bdd)
cur = conn.cursor()

req1 = "INSERT INTO client (nom, prenom) VALUES(?, ?)"
req2 = "INSERT INTO chambres (capacité, tarif) VALUES(?, ?)"

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

CAPACITE = (
  1,
  2,
  3,
  4,
  5,
  6
)

PRIX = (
  70,
  80,
  100,
  150,
  200
)

#for i in range(10):
#    p = choice(PRENOMS)
#    n = choice(NOMS)
#    cur.execute(req1, (n, p))

#for i in range(50):
#  c = choice(CAPACITE)
#  p = choice(PRIX)
#  cur.execute(req2, (c, p))


conn.commit()

cur.close()
conn.close()

class Query:
  ajouter_client = [
    '''
    INSERT INTO client (nom, prenom) VALUES(?, ?)
    '''
  ]