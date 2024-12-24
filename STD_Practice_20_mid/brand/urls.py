
from django.urls import path
from .views import CreateBrand
 

urlpatterns = [
    path('create/', CreateBrand.as_view(), name="create-brand"),
]  
