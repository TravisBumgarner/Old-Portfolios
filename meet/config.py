import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
mail_from = 'travis.bumgarner2@gmail.com'
mail_to = 'travis.bumgarner@gmail.com'
mail_key = 'xxygydmokdwlrvma'
