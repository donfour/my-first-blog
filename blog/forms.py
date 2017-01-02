from django import forms

from .models import Post

class PostForm(forms.ModelForm): #forms.ModelForm tells Django that PostForm is a model form

    class Meta:
        model = Post #which model should be used to create this form (model = Post)
        fields = ('title', 'text',)
