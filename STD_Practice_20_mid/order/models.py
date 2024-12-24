from django.db import models
from django.contrib.auth.models import User
from car_model.models import CarModel

# Create your models here.
class OrderModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.car.name
    