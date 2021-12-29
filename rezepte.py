import json
# https://www.w3schools.com/python/python_json.asp
# https://www.programiz.com/python-programming/json
# https://www.geeksforgeeks.org/json-dump-in-python/

# a Python object (dict):
rezepte = {
  "Kartoffelgratin": {
    "titel": "Kartoffel Gratin",
    "anzahl_personen": 2,
    "Zutaten":{
      "Kartoffel": (300, "g"),
      "Speck": (25, "g"),
      "Rahm": (75,"cl"),
      "Peterli": (10,"g"),
      "Rosmarin": (10,"g"),
      "Parmesan": (100,"g"),
      "Bouillon": (75,"cl"),
      "Knoblauch": (1,"Stück"),}},

  "Rüebliaufstrich": {
    "titel": "Rüebliaufstrich",
    "anzahl_personen": 2,
      "Zutaten":{
        "Tomatenpuree": (100,"g"),
        "Karotten" : (2, "Stück"),
        "Zwiebel" : (1, "Stück"),
        "Salz" : (1,"g"),
        "Olivenöl" : (10, "g"),
        "Cashew Nüsse" : (40, "g")}},

  "Gurkensalat": {
    "titel": "Gurkensalat",
    "anzahl_personen": 2,
      "Zutaten":{
        "Gurke" : (1, "Stück"),
        "Quark" : (50, "g"),
        "Salz" : (1, "g"),
        "Knoblauch" : (0.5, "Stück"),
        "Pfefferminze" : (1, "Stück")}},

  "Knödel" : {
    "titel": "Knädel",
    "anzahl_personen": 4,
      "Zutaten":{
        "Mutchli" : (10, "Stück"),
        "Salz" : (1, "g"),
        "Peffer" : (1, "g"),
        "Milch" : (50, "cl"),
        "Butter" : (100, "g"),
        "Peterli" : (1, "Stück"),
        "Ei" : (2, "Stück")}}


}


with open('rezepte.json', 'w') as f:
  json.dump(rezepte, f, indent=4, sort_keys=True)