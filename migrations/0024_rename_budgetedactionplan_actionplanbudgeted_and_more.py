# Generated by Django 5.0.7 on 2024-07-29 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rasmApp', '0023_remove_budgetedactionplan_erabudget_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BudgetedActionPlan',
            new_name='ActionPlanBudgeted',
        ),
        migrations.AlterModelTable(
            name='actionplanbudgeted',
            table='apbudgetedTb',
        ),
    ]
