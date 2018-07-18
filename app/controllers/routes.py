from app import app
from flask import render_template, redirect, request

from app.models.searchModel import searchModel
#from app.models.forms import LoginForm


@app.route("/", methods=['GET', 'POST'])
def index():
    form = searchModel()
    return render_template("index.html", title = "Balaio de Livros", form=form)