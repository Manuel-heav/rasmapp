# Generated by Django 5.0.7 on 2024-08-07 10:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rasmApp', '0028_apsummary_bapmonth'),
    ]

    operations = [
        migrations.AddField(
            model_name='accomplishment',
            name='budgetedap',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='rasmApp.budgetedap'),
        ),
    ]
