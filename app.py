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
    place = request.form["place"]
    max_results = int(request.form["max_results"])
    radius = float(request.form["radius"])
    sort = "sort" in request.form

    articles = functions.wikipedia_locationsearch(place=place, max_results=max_results, radius=radius, sort=sort)
    return render_template("results.html", articles=articles, place = place)