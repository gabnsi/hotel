from flask import Flask
from flask import render_template
from flask import request
from clients import Client

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/client', methods=['POST'])
def client():
    result = request.values  # méthode POST
    Nom = result['nom']
    Prenom = result['prenom']
    client = (None, Nom, Prenom)
    client.inserer_client()
#    return render_template("resultat.html",
#                           nom=nom,
#                           prenom=prenom)


app.run(debug=True, port=3579)
