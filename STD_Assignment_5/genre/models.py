from django.db import models

# Create your models here.
class BookGenre(models.Model):
    name = models.CharField(max_length=30, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"
    
    
    