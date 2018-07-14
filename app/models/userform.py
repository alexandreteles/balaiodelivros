from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, PasswordField,BooleanField, TextAreaField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Length

from app.models import tables

class signupform(FlaskForm):
    cpfuser = IntegerField("cpfuser", validators= [DataRequired()])
    name = StringField("name", validators= [DataRequired()])
    email = StringField("email", validators= [DataRequired()])
    password= PasswordField('password', validators=[
        DataRequired(),
        EqualTo('confirm_password')
    ])
    confirm_password = PasswordField('confirm_password')
    address = StringField("address", validators= [DataRequired()])
    dtbirth = StringField("dtbirth", validators= [DataRequired()])

    def validate_email(self, field):
        if tables.User.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')


class signinform(FlaskForm):

    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me')


class editprofileform(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    about_me = TextAreaField('about me', validators=[Length(min=0, max=140)])

