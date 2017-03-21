from flask import render_template
from app import app
from .forms import ContactForm

@app.route('/')
@app.route('/index')
def index():
    contact_form = ContactForm()
    #skills =  Skills.query.all()
    #skill_categories = Skill_Categories.query.all()
    return render_template('index.html', contact_form=contact_form)

