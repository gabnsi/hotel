from flask import Flask
from flask import render_template
from flask import request
from clients import Client, liste_client, liste_chambres

app = Flask(__name__)


@app.route('/')
def index():
    clients = liste_client()
    chambres = liste_chambres()
    return render_template("index.html", clients=clients, chambres=chambres)

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
    return render_template("resultat.html",
                           nom=Nom,
                           prenom=Prenom)


@app.route('/reserver', methods=['POST'])
def reserver():
    result = request.values  # méthode POST
    id_client=result['id_client']
    id_chambre=result['id_chambre']
    return render_template("ajouter_client.html",
                           id_client=id_client)


app.run(debug=True, port=3579)
