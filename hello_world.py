from flask import Flask
from flask import render_template
from flask import request

app = Flask("Hello World")

@app.route("/hello/", methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        ziel_nahrungsmittel = request.form['artikel']
        rueckgabe_string = ziel_nahrungsmittel

        ziel_menge = request.form['menge']
        rueckgabe_string = ziel_menge

        return render_template("foodstorage.html", artikelausgabe=rueckgabe_string)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)