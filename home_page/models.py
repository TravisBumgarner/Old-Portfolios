from django.db import models

class Project(models.Model):
	title = models.CharField(max_length=40)
	description = models.TextField()

class Tools(models.Model):
	projects = models.ManyToManyField(Project)



#TB
# A project is an object with object properties such as title, description, etc. 