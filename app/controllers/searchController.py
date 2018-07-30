from flask import flash, render_template, redirect, url_for, request
from app import app
from app.models import tables
from app.models.searchModel import searchModel


@app.route('/search', methods=['GET','POST'])
def search():
    form= searchModel()
    if form.validate_on_submit():
        return redirect(url_for('searchresults', search= form.search.data))


@app.route('/searchresults/<search>')
def searchresults(search):

        books = tables.Book.query.filter((tables.Book.title.like(search))|( tables.Book.author.like(search))|( tables.Book.type.like(search))|( tables.Book.phisicalstate.like(search))).all()

        print(books)
        return render_template('book/searchresults.html', books=books)
