from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.html5 import SearchField
from wtforms.validators import DataRequired

class searchModel(FlaskForm):
    search = StringField("search", validators= [DataRequired()])


