
from django.urls import path
from .views import CreateCarModel
 

urlpatterns = [
    path('create/', CreateCarModel.as_view(), name="car-create"),
]  
