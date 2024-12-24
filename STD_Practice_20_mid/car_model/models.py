from django.db import models
from brand.models import CarBrand

# Create your models here.
class CarModel(models.Model):
    image = models.ImageField(upload_to='cars/')
    name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    price = models.IntegerField()
    brand = models.ForeignKey(CarBrand,on_delete=models.CASCADE)
    description = models.CharField(max_length=30)
