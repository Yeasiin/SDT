from django.db import models
from book.models import BookModel

# Create your models here.
RATE_CHOICES = (
    ('1','1 Star'),
    ('2','2 Star'),
    ('3','3 Star'),
    ('4','4 Star'),
    ('5','5 Star')
)
class ReviewModel(models.Model):
    book = models.ForeignKey(BookModel, on_delete= models.CASCADE)
    name = models.CharField(max_length=30)
    rate = models.TextField(max_length=20, choices=RATE_CHOICES,default='5')
    comment = models.TextField()
    created_at = models.DateField(auto_now=True)
    
    
    def __str__(self):
        return f'Review from {self.name}'