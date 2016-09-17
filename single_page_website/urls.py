from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.project_list),
    #views.project_list refers to the function name in views.py
	url(r'^post/$', views.post_new_project),
    url(r'^new/$', views.view_new_project),
]