from app import app
from flask import render_template

#from app.models.table import User
from app.models.bookForm import BookForm


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print (form.username.data)
        print(form.password.data)
    else:
        print(form.errors)
    return render_template('login.html', form=form)


@app.route("/index/<user>")
@app.route("/", defaults={"user":None}, methods=['GET', 'POST'])
def index(user):
    return render_template('index.html', title="Balaio de Livros")

@app.route("/bookform", methods=["GET", "POST"])
def formbook():
    form = BookForm()
    if form.validate_on_submit():
        print(form.title.data)
        print(form.price.data)
    return render_template('bookform.html', title="Balaio de Livros", form = form)