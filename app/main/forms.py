from flask_wtf import FlaskForm
from wtforms.fields.core import StringField
from wtforms.fields.simple import SubmitField, TextAreaField
from wtforms.validators import Required
from wtforms_components import DateTimeField, DateField
from wtforms_components.fields.split_date_time import datetime_form
from wtforms_components.validators import DateRange
from datetime import date, datetime

class BookApp(FlaskForm):
  aptmnt_title = StringField('Subject')
  aptmnt_content = TextAreaField('Describe your Visit')
  aptmnt_when = DateField('Choose Date', validators=[Required()], render_kw={"placeholder": "YYYY-MM-DD"})
  submit = SubmitField('Book Now')