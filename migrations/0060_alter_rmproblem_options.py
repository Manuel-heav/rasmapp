# Generated by Django 5.0.7 on 2024-11-10 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rasmApp', '0059_alter_rfcclass_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rmproblem',
            options={'ordering': ['id']},
        ),
    ]
