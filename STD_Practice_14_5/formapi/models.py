from django.db import models

# Create your models here.
class ExampleModel(models.Model):
    id = models.AutoField(primary_key=True)
    
    name = models.CharField(max_length=50)
    email = models.EmailField()
    duration = models.DurationField()
    file = models.FileField(upload_to='files/')
    ip_addr = models.GenericIPAddressField()
    time = models.TimeField()
    url = models.URLField()
    uid = models.UUIDField()
    dob = models.DateTimeField()
    is_agree = models.BooleanField()    