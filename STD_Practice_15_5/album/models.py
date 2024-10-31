from django.db import models
from django.core import validators
from musician.models import MusicianModel

# Create your models here.
class AlbumModel(models.Model):
    class Meta:
        verbose_name = "Album"
        
    name = models.CharField(max_length=100,verbose_name="Album Name",validators=[validators.MinLengthValidator(3)])
    musician = models.ForeignKey(to=MusicianModel,on_delete=models.CASCADE,related_name='albums')
    release = models.DateTimeField(blank=True,auto_now_add=True)
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    rating = models.IntegerField(choices=RATING_CHOICES)
    
    def __str__(self) -> str:
        return f"Album: {self.name} Singer:{self.musician.f_name} {self.rating}"