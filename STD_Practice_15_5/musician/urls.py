from django.urls import path,include
from . import views

urlpatterns = [
    path("add/", views.add,name='add_musician'),
    path("update/<int:id>", views.update,name='update_musician'),
    path("delete/<int:id>", views.delete,name='delete_musician'),
]
