from django.forms import models
from .models import CategoryModel

class CategoryModelForm(models.ModelForm):
    class Meta:
        model = CategoryModel
        fields = "__all__"