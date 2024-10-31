from django import forms
from .models import AlbumModel


class AlbumModelForm(forms.ModelForm):
    class Meta:
        model = AlbumModel
        exclude =['release']