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
@app.route("/poke-info", methods=["GET", "POST"])
def results():
    name = request.values.get("name")
    name = name.replace(" ", "-")
    name = name.replace(":", "")
    name = name.replace(".", "")
    name = name.replace("'", "")

    poke_data = functions.get_pokemon_data(name=name)
    if poke_data != None: # if pokemon name creates successful API call
        name = name.title()
        poke_types = functions.pokemon_types(poke_data)
        weakness_dict = functions.weakness_calc(poke_types)

        splash_art = poke_data["sprites"]["other"]["official-artwork"]["front_default"]
        height = poke_data["height"]
        id = poke_data["id"]
        weight = poke_data["weight"]
        return render_template("poke-info.html", poke_data=poke_data, poke_types=poke_types, weakness_dict=weakness_dict,
                                                name=name, splash_art=splash_art, height=height, id=id, weight=weight)
    else: # if pokemon name did not match
        if functions.has_varieties(name): # if pokemon has a form that users need to specify (like if API does not like "apple" but wants "apple-red" or "apple-green")
            has_variety = True
            varieties = functions.varieties(name)
            return render_template("poke-info.html", poke_data=poke_data, name=name, has_variety=has_variety, varieties=varieties)
        else: # if pokemon name did not match anything in the API
            has_variety = False
            if len(name) > 15: # truncate name if long
                name = name[0:15] + "..."
            return render_template("poke-info.html", poke_data=poke_data, name=name, has_variety=has_variety)