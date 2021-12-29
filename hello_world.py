from flask import Flask
from flask import render_template
from flask import request
import daten


app = Flask("Hello World")


@app.route("/hello/", methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        ziel_menge = request.form['menge']

        ziel_mass = request.form['mass']

        ziel_article = request.form['article']

        daten.zutaten_speichern(ziel_menge, ziel_mass, ziel_article)

        return render_template("foodstorage.html",
                               artikelausgabe=ziel_menge + " " + ziel_mass + " " + ziel_article)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
