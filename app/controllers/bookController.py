from flask import abort, flash, redirect, url_for, render_template
from app import app, db
from app.models import tables
from app.models.bookForm import BookForm
from . import book

@book.route("/bookform", methods = ["GET", "POST"])
def addbook():
    form = BookForm()
    if form.validate_on_submit():
        book = Book(title=form.title.data, author=form.author.data, serie= form.serie.data, school= form.school.data, edition= form.edition.data, translateversion= form.translateversion.data, phisicalstate = form.phisicalstate.data, price = form.price.data)
        print(form.title.data)
        print(form.price.data)
        try:
            db.session.add(book)
            db.session.commit()
            flash('Voce adicionou um livro com sucesso!')
        except:
            flash('Erro ao adicionar livro')
            return render_template('bookform.html', title="Balaio de Livros", form = form)
    return render_template('listbooks.html', action ="Add", add_book=add_book, form=form, title="Add Book")

@book.route("/listbooks",  methods = ["GET", "POST"])
def listbook():
    books = Book.query.order_by(Book.title)
    return render_template('listbooks.html', books = books, title = 'Books')

#@book.route("/editbook",  methods = ["GET", "POST"])
#def editbook(id):

@book.route("/deletebook/<int:id>",  methods = ["GET", "POST"])
def deletebook(id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    flash('You have successfully deleted the book.')
    #return redirect(url_for('listbooks'))

	#eturn render_template(title="Delete Department")
