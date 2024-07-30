from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r"users", UserViewSet, basename="user")

urlpatterns = [
    path("api-token-auth/", views.obtain_auth_token),
    path("", include(router.urls)),
]
