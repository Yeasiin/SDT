from django.db import models
from category.models import CategoryModel

# Create your models here.
class TaskModel(models.Model):
    title = models.CharField(verbose_name="Task Title",max_length=100)
    desc = models.TextField(verbose_name="Description")
    is_complete = models.BooleanField(verbose_name="Is Completed",default=False)

    # To Select Category on Task level it need to be on Task Level
    categories = models.ManyToManyField('category.CategoryModel', related_name='tasks', blank=True)
    
    assign_date = models.DateTimeField(blank=True,auto_now_add=True)
    
    class Meta:
        verbose_name = "task"
        verbose_name_plural = "tasks"
    
    def __str__(self):
        return f"{self.title} - {"✅" if self.is_complete else "❌"}"
    