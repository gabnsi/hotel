from flask import Flask
from flask import render_template
from flask import request
from clients import Reservation, Client, liste_client, liste_chambres, liste_reservations

app = Flask(__name__)


@app.route('/')
def index():
    clients = liste_client()
    chambres = liste_chambres()
    reservations = liste_reservations()
    return render_template("index.html", clients=clients, chambres=chambres, reservations=reservations)

@app.route('/ajouter_client', methods=['POST'])
def ajouter_client():
    result = request.values  # méthode POST
    Nom = result['nom']
    Prenom = result['prenom']
    client = Client(None, Nom, Prenom)
    client.inserer_client()
    return render_template("ajouter_client.html",
                           nom=Nom,
                           prenom=Prenom)

@app.route('/supprimer_client', methods=['POST'])
def supprimer_client():
    result = request.values  # méthode POST
    Nom = result['nom']
    Prenom = result['prenom']
    client = Client(None, Nom, Prenom)
    client.supprimer_client()
    return render_template("supression_client.html",
                           nom=Nom,
                           prenom=Prenom)


@app.route('/reserver', methods=['POST'])
def Reserver():
    result = request.values  # méthode POST
    id_client=result['id_client']
    id_chambre=result['id_chambre']
    date_debut=result['date_debut']
    date_fin=result['date_fin']
    reservation = Reservation(None, id_client, id_chambre, date_debut, date_fin)
    reservation.reserver()
    return render_template("resultat.html",
                           id_client=id_client,
                           id_chambre=id_chambre,
                           date_debut=date_debut,
                           date_fin=date_fin,
                           )


app.run(debug=True, port=3579)
