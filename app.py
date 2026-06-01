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

    poke_data = functions.get_pokemon_data(name=name)
    return render_template("poke-info.html", poke_data=poke_data)