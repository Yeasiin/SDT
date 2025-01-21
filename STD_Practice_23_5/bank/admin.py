from django.contrib import admin
from .models import BankState

class BankStateAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        """Ensure only one instance of BankState can be added."""
        if BankState.objects.exists():
            return False
        return True
    
    def has_change_permission(self, request, obj=None):
        """Allow changes to the existing BankState."""
        return True
    
    def has_delete_permission(self, request, obj=None):
        """Prevent deletion of the only BankState."""
        return False

admin.site.register(BankState, BankStateAdmin)
