from django import forms
from .models import Post


class PostForm(forms.Form):
    model = Post
    fields = ('title', 'text',)
