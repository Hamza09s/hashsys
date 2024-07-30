from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from tenant_shared.models import Buisness
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    mobile_number = models.CharField(max_length=15)
    is_mobile_verified = models.BooleanField(default=False)
    buisness_name = models.CharField(max_length=255)

    buisness = models.OneToOneField(Buisness, on_delete=models.CASCADE)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
