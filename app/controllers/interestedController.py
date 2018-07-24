from flask import abort, flash, redirect, url_for, render_template, request
from flask_login import current_user, login_required

from app import app, db
from app.models import tables


@app.route("/interested/<id>",  methods = ["GET", "POST"])
@login_required
def interested(id):
    interest = tables.Interested.query.filter_by(book_id= id).first()
<<<<<<< HEAD
    if interest:
        user_id = interest.interested_id
        return redirect(url_for('user', id=user_id))
    else:
        return redirect(url_for('listbooks', id=current_user.id))
=======
    user_id = interest.interested_id
    return redirect(url_for('user', id=user_id))
>>>>>>> ffcbbf1ed35ba574f13b78c7189c745b88bbb44b

@app.route("/addinterest/<id>", methods =["GET", "POST"])
@login_required
def addinterest(id):
    interested_id = current_user.id
    book= tables.Book.query.get(id)
    interest = tables.Interested(owner_id = book.user_id, interested_id = interested_id, book_id = id)
    try:
        db.session.add(interest)
        db.session.commit()
        flash('Interesse registrado!')
    except:
        flash('Erro ao adicionar interesse')

    return redirect(url_for('user', id=book.user_id))