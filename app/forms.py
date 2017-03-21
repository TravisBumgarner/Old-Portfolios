from flask_wtf import Form
from wtforms import StringField, SelectMultipleField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, URL

class ContactForm(Form):
    first_name = StringField('first_name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])
    email_address = StringField('email', validators=[DataRequired(), Email()])
    website = StringField('website', validators=[URL()])
    topics = SelectMultipleField('topics', choices=[("mech_eng","Mechanical Engineering")])
    request = TextAreaField('request', validators=[DataRequired()])
    submit = SubmitField('submit')

