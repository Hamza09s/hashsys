from django.db import models
from accounts.models import CustomUser
from tenant_shared.models import Country, State, City
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=100)


class Brand(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="product_category",
    )
    brand = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="category_products",
    )
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, null=True, blank=True
    )
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
