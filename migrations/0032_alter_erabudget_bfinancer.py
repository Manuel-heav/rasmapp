# Generated by Django 5.0.7 on 2024-08-13 07:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rasmApp', '0031_alter_erabudget_bdistrict'),
    ]

    operations = [
        migrations.AlterField(
            model_name='erabudget',
            name='bfinancer',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='rasmApp.financer'),
        ),
    ]
