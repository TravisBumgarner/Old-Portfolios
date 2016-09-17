from django.conf.urls import url, include
from django.contrib import admin
urlpatterns = [
    url(r'^admin/', admin.site.urls), 
    url(r'', include('single_page_website.urls')),

    #This is the admin url which we've already visited
    #This line means that for every URL that starts with admin/, Django will find a corresponding view.
    # In this case we're including a lot of admin URLs so it isn't all packed into this small file – it's more readable and cleaner.
]



"""



^ for the beginning of the text
$ for the end of the text
\d for a digit
+ to indicate that the previous item should be repeated at least once
() to capture part of the pattern

Now imagine you have a website with the address like http://www.mysite.com/post/12345/, where 12345 is the number of your post.
Writing separate views for all the post numbers would be really annoying. 


We also want to keep the mysite/urls.py file clean, so we will import URLs from our project application to the main mysite/urls.py file. I, Travis, Won't do this.



urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
^$ symbolizes an empty place so it'll be the home page
name ='post_list' is the name of the URL that will be used to identify the view
it is important to name each url in the applicationtry to keep the names unique and easy to remember

"""