from django.db import models
from django.contrib.auth.models import  User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)




@receiver(post_save,sender=User)
def create_or_update_user_profile(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user = instance)
    instance.userprofile.save()








