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

from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    #  path("login/", views.user_login, name='login'),
     path('logout/',LogoutView.as_view(), name='logout'),
     path("register/",views.RegisterView.as_view(),name="register")
]
