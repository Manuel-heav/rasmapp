# Generated by Django 5.0.7 on 2024-10-19 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rasmApp', '0045_rmaactivity_remove_roadconditionsurvey_solution_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RMProblem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem', models.CharField(blank=True, default=None, max_length=100, null=True)),
            ],
            options={
                'db_table': 'ProblemTb',
            },
        ),
    ]
