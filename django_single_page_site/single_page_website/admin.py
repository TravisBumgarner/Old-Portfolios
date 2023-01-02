#to add, edit and delete the projects we've just we will use Django admin.

from django.contrib import admin
from .models import *
# Register your models here.

class photoUploadInline(admin.TabularInline):
	#Refers to inlines in ProjectAdmin where the model for adding a new image is Project_Image and
	# one extra field will be created when the post a new project page is opened
	model = Project_Image
	extra = 1

class projectLink(admin.TabularInline):
	#Refers to inlines in ProjectAdmin where the model for adding a new image is Project_Image and
	# one extra field will be created when the post a new project page is opened
	model = Project_Link
	extra = 1

class ProjectAdmin(admin.ModelAdmin):
	#Controls order of how things are displayed on Post a new project page
	fieldsets = [
		(None, {'fields': ['title']}),
		('Info',{'fields': ['created_date','summary','tools','categories',]}),
		('Media',{'fields': ['headline_image','video']})
	]
	#Let's me add an option to upload lots of images
	inlines = [photoUploadInline, projectLink]
	#let's projects be sorted by title and date
	list_display = ('title','created_date')
	#lelt's a filter for categories be added
	list_filter = ['categories']
	#Display many to many categories nicely
	filter_horizontal = ['tools','categories']


class SkillsCategoriesAdmin(admin.ModelAdmin):
	#let's projects be sorted by title and date
	list_display = ('title','order')

class About_Author_Link_Inline(admin.TabularInline):
	#Refers to inlines in ProjectAdmin where the model for adding a new image is Project_Image and
	# one extra field will be created when the post a new project page is opened
	model = About_Author_Link
	extra = 1

class About_Author_Admin(admin.ModelAdmin):
	inlines = [About_Author_Link_Inline]

admin.site.register(Project_Tool)
admin.site.register(Project_Category)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill)
admin.site.register(Skill_Category, SkillsCategoriesAdmin)
admin.site.register(About_Author, About_Author_Admin)
