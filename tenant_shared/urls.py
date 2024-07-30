from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework import routers
from tenant_shared.views import (
    CityViewSet,
    CountryViewSet,
    StateViewSet,
)

router = routers.DefaultRouter()
router.register(r"country", CountryViewSet, basename="country")
router.register(r"city", CityViewSet, basename="city")
router.register(r"state", StateViewSet, basename="state")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/account/", include("accounts.urls")),
    # path("api/shared/", include("tenant_shared.urls")),
    path("api/product/", include("products.urls")),
    path("api/shared/", include(router.urls)),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
