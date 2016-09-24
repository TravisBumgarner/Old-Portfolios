#All lines starting with from or import are lines that add some bits from other files. So instead of 
#copying and pasting the same things in every file, we can include some parts with from ... import ...


from django.db import models
from django.utils import timezone

class Project_Tool(models.Model):
    human_display_tool = models.CharField(max_length=100)
    html_class_display_tool = models.CharField(max_length=100)
    class Meta:
        ordering = ('human_display_tool',)

    def __str__(self):  
        return self.human_display_tool #self.title refers to title = models.CharField(max_length=200) line

class Project_Category(models.Model):
    human_display_category = models.CharField(max_length=100)
    html_class_display_category = models.CharField(max_length=100)
    class Meta:
        ordering = ('human_display_category',)

    def __str__(self):  
        return self.human_display_category #self.title refers to title = models.CharField(max_length=200) line

"""
Post_Project is how we refer to the data from the databse:
in the command line with ORM and Query Sets:

from single_page_website.models import Post_Project
Post_Project.objects.all()
"""
##################################################
########## Project Functions #####################
##################################################
class Project_Image(models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField()
    image = models.ImageField(upload_to = 'images_directory/')
    class Meta:
        ordering = ('title',)
    def __str__(self):  
        return self.title #self.title refers to title = models.CharField(max_length=200) line

class Project(models.Model):                       # This line defines our model, it is an object, class is a special keyword to define we are making an object
    author = models.ForeignKey('auth.User')             # models.Model means that the Post is a Django Model, so Django knows that it should be saved in the database.
    title = models.CharField(max_length=200)
    summary = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    tools = models.ManyToManyField(Project_Tool)
    categories = models.ManyToManyField(Project_Category)    
    headline_image = models.ImageField(upload_to = 'images_directory/headline_images' )
    project_images = models.ForeignKey(Project_Image, on_delete=models.CASCADE)
    class Meta:
        ordering = ('title',)

    #Publish is the name of the method for a post, it should be able to be published
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    #Methods often return something. There is an example of that in the __str__ method. In this scenario, when we call __str__() we will get a text (string) with a Post title.
    def __str__(self):  
        return self.title #self.title refers to title = models.CharField(max_length=200) line




##################################################
########## Skills Functions ######################
##################################################

class Skill_Category(models.Model):
    title = models.CharField(max_length=200)
    class Meta:
        ordering = ('title',)
    def __str__(self):  
        return self.title #self.title refers to title = models.CharField(max_length=200) line

class Skill(models.Model):
    title = models.CharField(max_length=200)
    rating = models.IntegerField()
    category = models.ForeignKey(Skill_Category, on_delete=models.CASCADE)
    class Meta:
        ordering = ('title',)
    def __str__(self):  
        return self.title #self.title refers to title = models.CharField(max_length=200) line




#TB
# A project is an object with >>object properties<< such as title, description, etc. 
# It should also have >>methods<< such as publish
# A >>model<< in Django is a special kind of object – it is saved in the database