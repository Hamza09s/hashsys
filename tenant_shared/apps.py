from django.apps import AppConfig


class TenantSharedConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tenant_shared'
