from django import forms
from .models import Post_Project

class Post_New_Project(forms.ModelForm):

    class Meta:
        model = Post_Project
        fields = ('title', 'summary','tools',)

        