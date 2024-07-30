from .models import Product, Category, Brand
from .serializers import BrandSerializer, CategorySerializer, ProductSerializer
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django_tenants.utils import schema_context


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        try:
            with schema_context(self.request.tenant.schema_name):
                return Product.objects.all()
        except Exception as e:
            raise APIException(f"An error occurred during creation: {str(e)}")

    def perform_create(self, serializer):
        try:
            with schema_context(self.request.tenant.schema_name):
                serializer.save(user=self.request.user)
        except Exception as e:
            raise APIException(f"An error occurred during creation: {str(e)}")

    def perform_update(self, serializer):
        try:
            with schema_context(self.request.tenant.schema_name):
                serializer.save()
        except Exception as e:
            raise APIException(f"An error occurred during creation: {str(e)}")

    def perform_destroy(self, instance):
        try:
            with schema_context(self.request.tenant.schema_name):
                instance.delete()
        except Exception as e:
            raise APIException(f"An error occurred during creation: {str(e)}")


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        try:
            with schema_context(self.request.tenant.schema_name):
                return Category.objects.all()
        except Exception as e:
            raise APIException(f"An error occurred during creation: {str(e)}")

    def perform_create(self, serializer):
        try:
            with schema_context(self.request.tenant.schema_name):
                serializer.save(user=self.request.user)
        except Exception as e:
            raise APIException(f"An error occurred during creation: {str(e)}")

    def perform_update(self, serializer):
        try:
            with schema_context(self.request.tenant.schema_name):
                serializer.save()
        except Exception as e:
            raise APIException(f"An error occurred during creation: {str(e)}")

    def perform_destroy(self, instance):
        try:
            with schema_context(self.request.tenant.schema_name):
                instance.delete()
        except Exception as e:
            raise APIException(f"An error occurred during creation: {str(e)}")


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        try:
            with schema_context(self.request.tenant.schema_name):
                return Brand.objects.all()
        except Exception as e:
            raise APIException(f"An error occurred during creation: {str(e)}")

    def perform_create(self, serializer):
        try:
            with schema_context(self.request.tenant.schema_name):
                serializer.save(user=self.request.user)
        except Exception as e:
            raise APIException(f"An error occurred during creation: {str(e)}")

    def perform_update(self, serializer):
        try:
            with schema_context(self.request.tenant.schema_name):
                serializer.save()
        except Exception as e:
            raise APIException(f"An error occurred during creation: {str(e)}")

    def perform_destroy(self, instance):
        try:
            with schema_context(self.request.tenant.schema_name):
                instance.delete()
        except Exception as e:
            raise APIException(f"An error occurred during creation: {str(e)}")
