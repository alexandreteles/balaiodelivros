from flask import abort, flash, redirect, url_for, render_template, request
from werkzeug.utils import secure_filename
import os

from app import app, db
from app.models import tables
from app.models.bookform import bookform
from config import APP_ROOT


@app.route("/bookform", methods = ["GET", "POST"])
def addbook():
    form = bookform()
    if form.validate_on_submit():
        book = tables.Book(user_cpf= 1234, title=form.title.data, author=form.author.data, serie= form.serie.data, school= form.school.data, edition= form.edition.data, translateversion= form.translateversion.data, phisicalstate = form.phisicalstate.data, price = form.price.data, type= form.type.data)
        print(form.title.data)
        print(form.price.data)
        try:
            db.session.add(book)
            db.session.commit()
            flash('Voce adicionou um livro com sucesso!')
        except:
            flash('Erro ao adicionar livro')

    return render_template('bookform.html',  title="Balaio de Livros", form = form)

@app.route("/bookform/editbook/<id>",  methods = ["GET", "POST"])
def editbook(id):
    book = tables.Book.query.filter_by(id= id).limit(1)
    form = bookform()
    if form.validate_on_submit():
        book = tables.Book(user_cpf= 1234, title=form.title.data, author=form.author.data, serie= form.serie.data, school= form.school.data, edition= form.edition.data, translateversion= form.translateversion.data, phisicalstate = form.phisicalstate.data, price = form.price.data, type= form.type.data)
        print(form.title.data)
        print(form.price.data)
        try:
            db.session.add(book)
            db.session.commit()
            flash('Voce editou um livro com sucesso!')
        except:
            flash('Erro ao editar livro')

    return render_template("bookform.html", form = form)

@app.route("/listbooks",  methods = ["GET", "POST"])
def listbooks():

    books = tables.Book.query.all()
    return render_template("listbooks.html", books=books)

@app.route("/listbooks/deletebook/<id>",  methods = ["GET", "POST"])
def deletebook(id):
    book = tables.Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    flash('You have successfully deleted the book.')
    return render_template("listbooks.html")


@app.route("/showbook/<id>", methods =["GET", "POST"])
def showbook(id):
    book = tables.Book.query.get(id)
    return render_template('showbook.html', book=book)


@app.route("/uploadImage",  methods = ["GET", "POST"])
def uploadImage():
    target = os.path.join(APP_ROOT, 'app/static/img/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)

    return render_template("complete.html")
