from django.db import models
from musician.models import Musician
from django.core import validators

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=50)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=5,
                                 validators=[validators.MaxValueValidator(5),
                                             validators.MinValueValidator(1)])
    
