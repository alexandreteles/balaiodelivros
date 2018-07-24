from flask import abort, flash, redirect, url_for, render_template, request
from flask_login import login_required, login_user, logout_user, current_user
from app import app, db
from app.models import tables
from app.models.userform import signupform, signinform, editprofileform
from datetime import datetime

@app.route("/signup", methods = ["GET", "POST"])
def signup():
    form = signupform()
    if form.validate_on_submit():

        user = tables.User(cpfuser= form.cpfuser.data, name= form.name.data, email= form.email.data, password= form.password.data, address= form.address.data, reputation = 0, dtbirth = datetime.strptime(form.dtbirth.data, '%d/%m/%Y'), grant= 0, about_me= form.about_me.data)
        try:
            print(form.email.data)
            db.session.add(user)
            db.session.commit()
            flash('O usuário foi registrado com sucesso')
            return redirect(url_for('signin'))
        except:
            print(form.errors)
            flash('Erro ao adicionar usuário')

    return render_template('user/signup.html',  title="Balaio de Livros", form=form)

@app.route("/signin", methods = ["GET", "POST"])
def signin():

    if current_user.is_authenticated:
       return redirect(url_for('index'))

    form = signinform()
    if form.validate_on_submit():
        user = tables.User.query.filter_by(email=form.email.data).first()

        if user.email and user.verify_password(form.password.data):
            print(form.errors)
            login_user(user)
            return redirect(url_for('index'))
        else:
            # login_user(user, remember=form.remember_me.data)
            flash('Email ou senha inválidos')

    return render_template('user/signin.html', form=form, title='Entrar')

@app.route('/signout')
@login_required
def signout():
    logout_user()
    flash('You have successfully been logged out')
    return redirect(url_for('signin'))

@app.route('/user/<id>')
@login_required
def user(id):
    user = tables.User.query.get(id)
    return render_template('user/user.html', user=user)

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = editprofileform()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        return redirect(url_for('user', id=current_user.id))
    elif request.method == 'GET':
        form.name.data = current_user.name
        form.about_me.data = current_user.about_me
    return render_template('user/edit_profile.html', title='Edit Profile',form=form)
