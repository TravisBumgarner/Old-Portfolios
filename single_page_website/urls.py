from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.project_list),
    #views.project_list refers to the function name in views.py
]