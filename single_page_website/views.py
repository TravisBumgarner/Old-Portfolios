#A view is a place where we put the "logic" of our application.
# It will request information from the model you created before and pass it to a template

from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import Post_New_Project

#Now is the moment when we have to include the model we have written in models.py.
# The dot before models means current directory or current application. 
#Both views.py and models.py are in the same directory. 
#This means we can use . and the name of the file (without .py). Then we import the name of the model (Post).
from .models import Post_Project

def home_page(request):
	return render(request, 'single_page_website/index.html',{})

def project_list(request):
	projects = Post_Project.objects.all()
	return render(request, 'single_page_website/index.html', {'projects':projects})
	#{}, is a place in which we can add some things for the template to use. 
	#{'projects':projects} is what can be played around with in HTML

def post_new_project(request):
	if request.method == "POST":
		form = Post_New_Project(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('view_new_project', pk=post.pk)
	else:
		form = Post_New_Project()
	return render(request, 'single_page_website/post_new_project.html', {'form':form})
		#form = Post_New_Project()
		#return render(request, 'single_page_website/post_new_project.html', {'form':form})
		#When we submit the form, we are brought back to the same view, but this time we have some more data in request, more specifically in request.POST
		#So in our view we have two separate situations to handle: first, when we access the page for the first time and we want a blank form, and second, 
		#when we go back to the view with all form data we just typed. So we need to add a condition (we will use if for that):
		
		#if request.method == "POST":
	    	#[...]
		#else:
	    	#form = PostForm()

def view_new_project(request):
	return render(request, 'single_page_website/index.html',{})
	#{}, is a place in which we can add some things for the template to use. 
	#{'projects':projects} is what can be played around with in HTML
