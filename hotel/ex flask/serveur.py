from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/resultat', methods=['GET', 'POST'])
def resultat():
    result = request.values  # méthode POST
    nom = result['nom']
    prenom = result['prenom']
    print(nom, prenom)
    return render_template("resultat.html",
                           nom=nom,
                           prenom=prenom)


@app.route('/vehicule')
def vehicule():
    result = request.args  # méthode GET
    marque = result['marque']
    couleur = result['couleur']
    print(marque, couleur)
    return render_template('vehicule.html',
                           marque=marque,
                           couleur=couleur)


app.run(debug=True, port=3579)
