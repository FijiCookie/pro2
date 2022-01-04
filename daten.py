import json


def speichern(file, key, menge, mass, article):
    try:
        with open(file) as open_file:
            file_inhalt = json.load(open_file)
    except FileNotFoundError:
        file_inhalt = {}

    file_inhalt[str(key)] = {
        "Menge": menge,
        "Mass": mass,
        "Article": article
    }

    with open(file, "w") as open_file:
        json.dump(file_inhalt, open_file, indient=4, sort_keys=True)


def zutaten_speichern(menge, mass, article):
    file_name = "zutaten_daten.json"
    speichern(file_name, menge, mass, article)
    return menge, mass, article


def zutaten_laden():
    file_name = "zutaten_daten_2.json"

    try:
        with open(file_name) as open_file:
            file_inhalt = json.load(open_file)
    except FileNotFoundError:
        file_inhalt = {}

    return file_inhalt
