from django import forms
from django.forms import fields

from .models import PostModel


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ["title", "description", "date"]


class RawPostForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    date = forms.DateField()
