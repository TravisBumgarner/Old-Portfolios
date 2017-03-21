from app import app, db

from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin

from .models import Author, AuthorLink
from .models import Skills, SkillCategories
from .models import Project, ProjectCategories, ProjectImages, ProjectLinks, ProjectsToCategories, ProjectsToTools, ProjectTools

admin = Admin(app)
admin.add_view(ModelView(Author, db.session))
admin.add_view(ModelView(AuthorLink, db.session))

admin.add_view(ModelView(Skills, db.session))
admin.add_view(ModelView(SkillCategories, db.session))

admin.add_view(ModelView(Project, db.session))
admin.add_view(ModelView(ProjectTools, db.session))
admin.add_view(ModelView(ProjectCategories, db.session))
admin.add_view(ModelView(ProjectLinks, db.session))
admin.add_view(ModelView(ProjectImages, db.session))