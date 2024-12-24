from django.contrib import admin
from django.urls import path,include
from user.views import UserLoginView
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView, orders, SingleProduct
from user.views import UserUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomeView.as_view(), name="home"),
    path("product/<int:pk>",SingleProduct.as_view(),name="single-product"),
    
    path("profile/update/", UserUpdateView.as_view(), name='profile-update'),
    path("profile/order/", orders, name="orders"),
    path("brand/", include('brand.urls')),
    path("model/",include('car_model.urls')),
    
    path("auth/login/", UserLoginView.as_view(), name='login'),
    path("auth/", include('django.contrib.auth.urls')),
    path('auth/', include('user.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
