from django.db import models
from django.core import validators

# Create your models here.
class MusicianModel(models.Model):
    class Meta:
        verbose_name = 'Musician'

    f_name = models.CharField(max_length=100,verbose_name='First Name',validators=[validators.MinLengthValidator(3)])
    l_name = models.CharField(max_length=100,verbose_name='Last Name',validators=[validators.MinLengthValidator(3)])
    email = models.EmailField(verbose_name='Email Address',validators=[validators.MinLengthValidator(5)])
    phone = models.CharField(max_length=15,verbose_name='Phone Number')
    instrument = models.CharField(max_length=100,verbose_name='Instrument Type')
    
    
    def __str__(self) -> str:
        return f"{self.f_name} {self.l_name} - {self.instrument}"