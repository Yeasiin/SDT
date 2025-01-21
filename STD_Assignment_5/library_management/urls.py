from django.contrib import admin
from django.urls import path,include
from .views import HomeView, SingleProduct,borrows
from user.views import UserUpdateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomeView.as_view(), name="home"),
    path("book/<int:pk>",SingleProduct.as_view(),name="single-product"),
    path("profile/update/", UserUpdateView.as_view(), name='profile-update'),
    path("profile/borrows/", borrows, name="borrows"),
    path('auth/', include('user.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
