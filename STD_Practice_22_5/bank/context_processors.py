from .models import BankState

def bank_state(request):
    """Context processor to add BankState to every template."""
    bank_state = BankState.objects.first()  # Get the single instance
    return {'bank_state': bank_state}