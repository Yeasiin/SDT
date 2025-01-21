from django.forms import ModelForm
from .models import ReviewModel
from django import forms


class ReviewForm(ModelForm):
    class Meta:
        model  = ReviewModel
        fields = ['name','rate','comment']
        
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))

