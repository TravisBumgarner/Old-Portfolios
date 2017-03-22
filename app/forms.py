from flask_wtf import Form
from wtforms import StringField, SelectMultipleField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, URL

class ContactForm(Form):
    name = StringField('name', validators=[DataRequired()])
    email_address = StringField('email', validators=[DataRequired(), Email()])
    website = StringField('website', validators=[URL()])
    request = TextAreaField('request', validators=[DataRequired()])
    submit = SubmitField('submit')

