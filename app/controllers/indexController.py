from flask import render_template, redirect, request, url_for
from app import app
from app.models.searchModel import searchModel

@app.route("/", methods=['GET', 'POST'])
def index():
        form= searchModel()
        return render_template("index.html", title = "Balaio de Livros", form =form)

@app.route("/didatic", methods=['GET', 'POST'])
def didatic():
    return redirect(url_for('searchresults', search="Didatico"))

@app.route("/paradidatic", methods=['GET', 'POST'])
def paradidatic():
    return redirect(url_for('searchresults', search="Paradidatico"))