from django.db import models
from django.contrib.auth.models import User
from book.models import BookModel

# Create your models here.
class BorrowModel(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE)
    balance_after_record = models.IntegerField()
    is_returned = models.BooleanField(default=False)
    created_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.book.title