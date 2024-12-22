"""
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #  path("add/",views.create,name='add_musician')
     path("add/",views.CreateMusicianView.as_view(),name='add_musician'),
     path('update/<int:pk>/',views.UpdateMusicianView.as_view(),name="update_musician"),
     path('delete<int:pk>/',views.DeleteMusicianView.as_view(),name="delete_musician")
]
