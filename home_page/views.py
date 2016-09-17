from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, loader
from django.http import Http404
from .forms import PostProject
from django.shortcuts import redirect
from .models import Project

# Create your views here.
def home_page(request):
	return render(request, 'home_page/index.html', {})

def project_list(request):
	projects = Project
	return render(request, 'home_page/index.html', {'posts':projects} )

def post_project(request):
	if request.method =="POST":
		project = PostProject(request.POST)
		if project.is_valid():
			post = project.save(commit = True)
			post.save()
			return redirect('../index.html', pk = post.pk)
		else:
			form = PostProject()
	return render(request, 'home_page/post_project.html',{'form':PostProject})

