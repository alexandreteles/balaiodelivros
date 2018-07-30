from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email

class saleform(FlaskForm):
    #book = StringField('book', validators=[DataRequired()])
    client_mail = StringField('client_mail', validators=[DataRequired(), Email()])

