from django.db import models
from django_tenants.models import TenantMixin, DomainMixin


class Buisness(TenantMixin):
    name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)

    auto_create_schema = True


class Domain(DomainMixin):
    pass


class Country(models.Model):
    name = models.CharField(max_length=100)


class State(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, null=True, blank=True
    )


class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True, blank=True)
