from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DecimalField, TextAreaField, RadioField
from wtforms.validators import DataRequired, regexp

class bookform(FlaskForm):
    title = StringField("title", validators= [DataRequired()])
    author = StringField("author", validators= [DataRequired()])
    serie = StringField("serie", validators= [DataRequired()])
    school = StringField("school")
    edition = StringField("edition", validators= [DataRequired()])
    translateversion = StringField("translateversion")
    phisicalstate = TextAreaField("phisicalstate", validators= [DataRequired()])
    price = DecimalField("price", validators= [DataRequired()])
    type = RadioField("type", choices= [('Didatico','Didatico'),('Paradidatico','Paradidatico')], validators= [DataRequired()])
    #choices=[("label", "valor")]


