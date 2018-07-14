from flask import abort, flash, redirect, url_for, render_template, request
from flask_login import current_user, login_required

from app import app, db
from app.models import tables
from app.models.bookform import bookform


@app.route("/interested/<id>",  methods = ["GET", "POST"])
@login_required
def interested(id):
    interest = tables.Interested.query.filter_by(book_id= id)
    user = interest.interested_id
    return render_template("user/<id>", user = user)