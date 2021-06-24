from flask_wtf import FlaskForm
from wtforms.fields.core import DateField, StringField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import Required

class BookApp(FlaskForm):
  aptmnt_title = StringField('Subject')
  aptmnt_content = TextAreaField('Describe your Visit')
  aptmnt_when = DateField('Choose Date', validators=[Required(), ])