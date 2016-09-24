#to add, edit and delete the projects we've just we will use Django admin.

from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Project)
admin.site.register(Project_Tool)
admin.site.register(Project_Category)
admin.site.register(Project_Image)
admin.site.register(Skill)
admin.site.register(Skill_Category)