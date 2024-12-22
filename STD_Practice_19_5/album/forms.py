from .models import Album
from django.forms import ModelForm


class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = "__all__"
