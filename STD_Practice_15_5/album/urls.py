from django.urls import path,include
from . import views

urlpatterns = [
    path("add/", views.add,name='add_album'),
    path("update/<int:id>", views.update,name='update_album'),
]
