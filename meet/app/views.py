from flask import render_template, request, redirect, flash, url_for
from app import app, db
from gmail import GMail, Message
import datetime

from config import mail_key, mail_to, mail_from
from .models import Message as DB_Message
from .forms import ContactForm

@app.route('/', methods = ['GET', 'POST'])
def index():
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        db_message = DB_Message(
            name = contact_form.name.data,
            date = datetime.datetime.now(),
            message = contact_form.message.data,
            email = contact_form.email_address.data,
            website = contact_form.website.data
        )
        db.session.add(db_message)
        db.session.commit()

        gmail = GMail(mail_from, mail_key)
        msg = """
                Name: {} <br>
                Website: {} <br>
                Email: {} <br>
                Message: {}
            """.format(contact_form.name.data,
                       contact_form.website.data,
                       contact_form.email_address.data,
                       contact_form.message.data)

        gmail.send(Message('Message from {}'.format(contact_form.email_address.data), to= mail_to, html=msg))
        flash('Thank you for your message. I will be in touch soon!')
        return redirect(url_for('index', _anchor="contact"))
    return render_template('index.html', contact_form=contact_form)

