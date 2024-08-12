"""
URL configuration for PTIBackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from users.views import UpdateProfileView, UserViewSet, UserLogIn, create_auth

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/products/", include("products.urls")),
    path("api/categories/", include("categories.urls")),
    path("api/orders/", include("orders.urls")),
    path('api/v1/', include(router.urls)),
    path('api/user-login/', UserLogIn.as_view()),
    path('api/register/', create_auth),
    path('api/update-profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),
]