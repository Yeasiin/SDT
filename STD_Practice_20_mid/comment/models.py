from django.db import models
from car_model.models import CarModel

# Create your models here.
class CommentModel(models.Model):
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    comment = models.CharField(max_length=500)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'Comment from {self.name}'
    