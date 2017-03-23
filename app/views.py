from flask import render_template, request, redirect, flash, url_for
from app import app
from .forms import ContactForm
from gmail import GMail, Message
from config import mail_key, mail_to, mail_from


@app.route('/', methods = ['GET', 'POST'])
def index():
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
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

