# Generated by Django 5.0.7 on 2024-08-13 07:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rasmApp', '0032_alter_erabudget_bfinancer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='erabudget',
            name='bproject',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='rasmApp.projecttype'),
        ),
    ]
