#to add, edit and delete the projects we've just we will use Django admin.

from django.contrib import admin
from .models import Post_Project, Tool
# Register your models here.

admin.site.register(Post_Project)
admin.site.register(Tool)