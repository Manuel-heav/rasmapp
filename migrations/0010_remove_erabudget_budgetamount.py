# Generated by Django 5.0.7 on 2024-07-25 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rasmApp', '0009_alter_erabudget_budgetamount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='erabudget',
            name='budgetamount',
        ),
    ]
