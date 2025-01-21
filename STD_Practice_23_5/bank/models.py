from django.db import models
from django.core.exceptions import ValidationError

class BankState(models.Model):
    bank_name = models.CharField(max_length=255)
    bank_logo = models.ImageField(upload_to='static/bank_logos/')
    bank_operational = models.BooleanField(default=True)

    def clean(self):
        """Ensure only one instance of BankState exists."""
        if not self.pk and BankState.objects.exists():
            raise ValidationError("There can be only one instance of BankState.")
    
    def save(self, *args, **kwargs):
        # Ensure only one instance of BankState exists
        if not self.pk and BankState.objects.exists():
            raise ValidationError("There can only be one instance of BankState.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.bank_name