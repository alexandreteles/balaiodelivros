from flask import flash, redirect, url_for, render_template, request, jsonify
from flask_login import login_required, current_user

from app import app, db
from app.models import tables
from app.models.saleform import saleform

@app.route("/sale/<id>", methods= ['GET', 'POST'])
@login_required
def sale(id):
    form = saleform()
    book = tables.Book.query.get(id)

    if form.validate_on_submit():
        client = tables.User.query.filter_by(email=form.client_mail.data).first()
        print(client.email)
        sale = tables.Sale(vendor_id= current_user.id, client_id=client.id, book_id=id)
        book.sold = 1
        try:
            db.session.add(sale)
            db.session.commit()
            flash('Venda registrada!')
            return redirect(url_for('listbooks',id=current_user.id))
        except:
            flash('Erro ao registrar venda')
        #return redirect(url_for('listbooks', id=current_user.id))
    return render_template("sale/sale.html", form=form, book=book)
