from hotel import Query
import sqlite3

fichier_BDD = 'bdd.db'


class Client():

    def __init__(self, id_client, nom, prenom):
        self.id_client = id_client
        self.nom = nom
        self.prenom = prenom
    
    def id_client(self):
        return self.id_client

    def inserer_client(self):
        req1 = "INSERT INTO client (nom, prenom) VALUES(?, ?)"
        conn = sqlite3.connect(fichier_BDD)
        cur = conn.cursor()
        cur.execute(req1, (self.nom, self.prenom))
        conn.commit()
        cur.close()
        conn.close()

    def supprimer_client(self):
        req = "DELETE FROM client WHERE nom = ? and prenom = ?"
        conn = sqlite3.connect(fichier_BDD)
        cur = conn.cursor()
        cur.execute(req, (self.nom, self.prenom))
        conn.commit()
        cur.close()
        conn.close()


# c = Client(None, "mat", "rel")
# c.inserer_client()
def liste_client():
    req2 = "SELECT id_client, nom, prenom FROM client "
    conn = sqlite3.connect(fichier_BDD)
    cur = conn.cursor()
    cur.execute(req2)
    clients = cur.fetchall()
    cur.close()
    conn.close()
    return clients


class Chambres():

    def __init__(self, id_chambre, capacite, tarif):
        self.id_chambre = id_chambre
        self.capacite = capacite
        self.tarif = tarif

    def id_chambre(self):
        return self.id_chambre

    def capacite(self):
        return self.capacite

    def tarif(self):
        return self.tarif

def liste_chambres():
    req3 = "SELECT id_chambre, capacité, tarif FROM chambres "
    conn = sqlite3.connect(fichier_BDD)
    cur = conn.cursor()
    cur.execute(req3)
    chambres = cur.fetchall()
    cur.close()
    conn.close()
    return chambres


class Reservation:

    def __init__(self, id_reservation, id_client, id_chambre, date_debut, date_fin):
        self.id_client = id_client
        self.id_chambre = id_chambre
        self.date_debut = date_debut
        self.date_fin = date_fin

    def reserver(self):
        req4 = '''INSERT INTO "reservation"
            ("id_client", "id_chambre", "date_debut", "date_fin")
            VALUES (?, ?, ?, ?);'''
        conn = sqlite3.connect(fichier_BDD)
        cur = conn.cursor()
        cur.execute(req4, (self.id_client, self.id_chambre, self.date_debut, self.date_fin))
        conn.commit()
        cur.close()
        conn.close()

#r = Reservation(None, 11, 24, '2022-14-11', '2022-17-11')
#r.reserver()

def liste_reservations():
    req5 = "SELECT id_chambre, date_debut, date_fin FROM reservation "
    conn = sqlite3.connect(fichier_BDD)
    cur = conn.cursor()
    cur.execute(req5)
    reservations = cur.fetchall()
    cur.close()
    conn.close()
    return reservations
