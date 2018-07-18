from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    cpfuser = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    pw_hash = db.Column(db.String(80))
    address = db.Column(db.Text, nullable=False)
    reputation = db.Column(db.Float)
    dtbirth = db.Column(db.Date)
    grant = db.Column(db.Integer)
    about_me = db.Column(db.String(140))

    def __init__(self, cpfuser, name, email, address, reputation, dtbirth, grant, password, about_me):
        self.name = name
        self.cpfuser = cpfuser
        self.email = email
        self.address = address
        self.reputation = reputation
        self.dtbirth = dtbirth
        self.grant = grant
        self.pw_hash = generate_password_hash(password)
        self.about_me = about_me
    
    def verify_password(self, password):
        """
        verifica se o hash corresponde a senha
        """
        return check_password_hash(self.pw_hash, password)
    
    def __repr__(self):
        return "<User %r>" % self.name

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    serie = db.Column(db.String(80), nullable=False)
    school = db.Column(db.String(80), nullable=False)
    edition =   db.Column(db.String(80), nullable=False)
    translateversion = db.Column(db.String(80))
    phisicalstate = db.Column(db.Text, nullable=False)
    type = db.Column(db.String(80), nullable=False)
    #sold = db.Column(db.Integer)
    price = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    
    user = db.relationship('User', foreign_keys = user_id)

    def __init__ (self, title, author, serie, school, edition, translateversion, phisicalstate, price, user_id, type):
        self.title = title
        self.author = author
        self.serie = serie
        self.school = school
        self.edition = edition
        self.translateversion = translateversion
        self.phisicalstate = phisicalstate
        self.price = price
        self.user_id= user_id
        self.type = type

    def __repr__(self):
        return "<Book %r>" % self.title     

class Interested(db.Model):
    __tablename__ = "interested"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    interested_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))

    user = db.relationship('User', foreign_keys = owner_id)
    user2 = db.relationship('User', foreign_keys=interested_id)
    book = db.relationship('Book', foreign_keys = book_id)

    def __init__ (self, owner_id, book_id, interested_id):
        self.owner_id = owner_id
        self.interested_id = interested_id
        self.book_id = book_id
    
    def __repr__(self):
        return "<Interest %r>"% self.book_id
    
class Ad(db.Model):
    __tablename__ = "ads"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))

    user = db.relationship('User', foreign_keys = user_id)
    book = db.relationship('Book', foreign_keys = book_id)

    def __init__ (self, user_id, book_id):
        self.user_id = user_id
        self.book_id = book_id
    
    def __repr__(self):
        return "<Interest %r>"% self.book_id

class BookImage(db.Model):
    __tablename__ = "bookimages"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    data = db.Column(db.LargeBinary)
    name = db.Column(db.String(80))
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))

    book = db.relationship('Book', foreign_keys=book_id)

    def __init__(self, data, name, book_id):
        self.data = data
        self.name= name
        self.book_id = book_id

