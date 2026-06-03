# Justin Nguyen
# HCDE 310 Professor Shengzhi Wang
# Final Project P3: Pokemon Infographic

import functions

from flask import Flask, render_template, request

app = Flask(__name__)


# homepage
@app.route("/")
def index():
    return render_template("index.html")


# pokemon info page
@app.route("/poke-info", methods=["POST"])
def results():
    name = request.form["name"]
    name = name.replace(" ", "-")
    name = name.replace(":", "")
    name = name.replace(".", "")
    name = name.replace("'", "")

    poke_data = functions.get_pokemon_data(name=name)
    if poke_data != None:
        name = name.title()
        poke_types = functions.pokemon_types(poke_data)
        weakness_dict = functions.weakness_calc(poke_types)

        for i in range(len(poke_types)):
            poke_types[i] = poke_types[i].title()
        splash_art = poke_data["sprites"]["other"]["official-artwork"]["front_default"]
        height = poke_data["height"]
        id = poke_data["id"]
        weight = poke_data["weight"]
        return render_template("poke-info.html", poke_data=poke_data, poke_types=poke_types,weakness_dict=weakness_dict,
                                                name=name, splash_art=splash_art, height=height, id=id, weight=weight)
    else:
        if len(name) > 15:
            name = name[0:15] + "..."
        return render_template("poke-info.html", poke_data=poke_data, name=name)