from django import forms

from .models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['body']
        labels = {
            'body': 'Express yourself'
        }
        widgets = {
            'body': forms.Textarea(attrs={'style': 'height: 5em; width: 90%; margin: 0 auto; word-wrap: break-word;'}),
        }