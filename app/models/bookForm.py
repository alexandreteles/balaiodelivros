from flask_wtf import FlaskForm
from flask_uploads import UploadSet, IMAGES
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, BooleanField, DecimalField, TextAreaField
from wtforms.validators import DataRequired
#from wtforms.validators import Regexp

class BookForm(FlaskForm):
    title = StringField("title", validators=[DataRequired()])
    author = StringField("author",  validators=[DataRequired()])
    serie = StringField("serie",  validators=[DataRequired()])
    school = StringField("school")
    edition = StringField("edition",  validators=[DataRequired()])
    translateversion = StringField("translateversion")
    phisicalstate = StringField("phisicalstate",  validators=[DataRequired()])
    price = DecimalField("price",  validators=[DataRequired()])

class UploadForm(FlaskForm):
   # image        = FileField(u'Image File', [validators.regexp(u'^[^/\\]\.jpg$')])
    description  = TextAreaField(u'Image Description')

    def validate_image(form, field):
        if field.data:
            field.data = re.sub(r'[^a-z0-9_.-]', '_', field.data)

def upload(request):
    form = UploadForm(request.POST)
    if form.image.data:
        image_data = request.FILES[form.image.name].read()
        open(os.path.join(UPLOAD_PATH, form.image.data), 'w').write(image_data)