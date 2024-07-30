# Generated by Django 5.0.7 on 2024-07-30 07:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenant_shared', '0002_add_localhostdomain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tenant_shared.state'),
        ),
        migrations.AlterField(
            model_name='state',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tenant_shared.country'),
        ),
    ]
