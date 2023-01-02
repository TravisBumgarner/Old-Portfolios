from flask_wtf import Form
from wtforms import DateField, StringField, SelectMultipleField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, URL, Optional
import datetime

class ContactForm(Form):
    name = StringField('name', validators=[DataRequired()])
    email_address = StringField('email', validators=[DataRequired(), Email()])
    website = StringField('website', validators=[URL(), Optional()])
    message = TextAreaField('request', validators=[DataRequired()])
    submit = SubmitField('submit')

