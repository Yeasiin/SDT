from django.db import models
from django.core import validators

# Create your models here.
class CategoryModel(models.Model):
    name = models.CharField(verbose_name="Category Name",max_length=100,validators=[validators.MinLengthValidator(3)])
    # To Select Category on task creation this need to be on task level
    # tasks = models.ManyToManyField(TaskModel,related_name='categories')
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
    def __str__(self) -> str:
        return self.name