from django.db import migrations, models
from tenant_shared.models import Buisness, Domain


def create_initial_data(apps, schema_editor):
    buisness = Buisness.objects.create(name="Public", schema_name="public")

    Domain.objects.create(domain="localhost", tenant=buisness, is_primary=True)


class Migration(migrations.Migration):

    dependencies = [
        (
            "tenant_shared",
            "0001_initial",
        ),
    ]

    operations = [
        migrations.RunPython(create_initial_data),
    ]
