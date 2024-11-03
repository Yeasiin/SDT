from django.forms import models
from .models import TaskModel

class TaskModelForm(models.ModelForm):
    class Meta:
        model = TaskModel
        fields = "__all__"