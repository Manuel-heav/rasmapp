# Generated by Django 5.0.7 on 2024-07-25 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rasmApp', '0012_alter_erabudget_budgetamount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='erabudget',
            name='budgetamount',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
