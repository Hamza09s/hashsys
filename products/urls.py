from email.mime import base
from posixpath import basename
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BrandViewSet, CategoryViewSet, ProductViewSet

router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="product")
router.register(r"brand", BrandViewSet, basename="brand")
router.register(r"category", CategoryViewSet, basename="category")
urlpatterns = [
    path("", include(router.urls)),
]
