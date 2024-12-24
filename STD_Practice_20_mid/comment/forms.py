from django.forms import ModelForm
from .models import CommentModel
from django import forms


class CommentForm(ModelForm):
    class Meta:
        model  = CommentModel
        fields = ['name','comment']
        
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))

