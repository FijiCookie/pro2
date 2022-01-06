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

        alles= [["ziel_menge1", "ziel_mass1", "ziel_article1"], ["ziel_menge2", "ziel_mass2", "ziel_article2"], ["ziel_menge3", "ziel_mass3", "ziel_article3"]]

        daten.zutaten_speichern(alles)

        return render_template("foodstorage.html",
                               artikelausgabe=(alles))

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
