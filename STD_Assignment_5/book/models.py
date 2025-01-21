from django.db import models
from genre.models import BookGenre
from django.contrib.auth.models import User


# Create your models here.
class BookModel(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='books/')
    quantity = models.IntegerField()
    price = models.IntegerField()
    genres = models.ManyToManyField(BookGenre)
    description = models.CharField(max_length=130)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
    
    
    