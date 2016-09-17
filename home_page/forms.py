from django import forms

from .models import Project

class PostProject(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('title', 'description',)