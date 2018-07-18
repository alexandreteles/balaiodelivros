from flask import flash, render_template, redirect, url_for, request
from app import app
from app.models import tables
from app.models.searchModel import searchModel


@app.route('/search', methods=['GET','POST'])
def search():
    form= searchModel()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return redirect(url_for('searchresults', search= form.search.data))


@app.route('/searchresults/<search>')
def searchresults(search):
    form = searchModel()
    if form.validate_on_submit():
        results = tables.Book.query.filter(( tables.Book.title== search)|(tables.Book.author == search)|(tables.Book.type == search)).all()
        return render_template('book/searchresults.html', title="Balaio de Livros", results=results)
