#A view is a place where we put the "logic" of our application.
# It will request information from the model you created before and pass it to a template

from django.shortcuts import render, redirect
from django.utils import timezone
from .models import *

#Now is the moment when we have to include the model we have written in models.py.
# The dot before models means current directory or current application. 
#Both views.py and models.py are in the same directory. 
#This means we can use . and the name of the file (without .py). Then we import the name of the model (Post).

def home_page(request):
	return render(request, 'single_page_website/index.html',{})

def project_list(request):
	projects = Project.objects.all().order_by('-created_date')
	skills = Skill.objects.all()
	skills_category = Skill_Category.objects.all()
	about = About_Author.objects.all()[0]
	about_links = About_Author_Link.objects.all()
	return render(request, 'single_page_website/index.html', {'projects':projects,'skills_category':skills_category,'skills':skills,'about':about,'links':about_links})
	#{}, is a place in which we can add some things for the template to use. 
	#{'projects':projects} is what can be played around with in HTML


def view_new_project(request):
	return render(request, 'single_page_website/index.html',{})
	#{}, is a place in which we can add some things for the template to use. 
	#{'projects':projects} is what can be played around with in HTML
