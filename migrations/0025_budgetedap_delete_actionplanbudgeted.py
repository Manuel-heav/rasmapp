# Generated by Django 5.0.7 on 2024-07-29 06:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rasmApp', '0024_rename_budgetedactionplan_actionplanbudgeted_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BudgetedAP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bapmonth', models.CharField(blank=True, choices=[('መስከረም', 'መስከረም'), ('ጥቅምት', 'ጥቅምት'), ('ህዳር', 'ህዳር'), ('ታህሳስ', 'ታህሳስ'), ('ጥር', 'ጥር'), ('የካቲት', 'የካቲት'), ('መጋቢት', 'መጋቢት'), ('ሚያዚያ', 'ሚያዚያ'), ('ግንቦት', 'ግንቦት'), ('ሰኔ', 'ሰኔ'), ('ሐምሌ', 'ሐምሌ'), ('ነሐሴ', 'ነሐሴ')], max_length=20, null=True)),
                ('bapinBr', models.FloatField(blank=True, default=None, null=True)),
                ('bapinKm', models.FloatField(blank=True, default=None, null=True)),
                ('bremark1', models.CharField(blank=True, choices=[('01', 'በጦርነቱ/በፀጥታ ችግር ምክንያት'), ('02', 'በኮንትራት የሚተዳደሩ ፕሮጀክቶች በመቋረጣቸው ምክንያት'), ('03', 'በግዢ ሂደት ላይ ያሉ ፕሮጀክቶች'), ('04', 'በግብአት እጥረት ምክንያት'), ('05', 'በመንገድ ወሰን ማስከበር ምክንያት'), ('06', 'የተለያየ (Others)')], max_length=100, null=True)),
                ('bremark2', models.TextField(blank=True, default=None, null=True)),
                ('erabudget', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='rasmApp.erabudget')),
            ],
            options={
                'db_table': 'budgetedAPTb',
                'ordering': ['id'],
            },
        ),
        migrations.DeleteModel(
            name='ActionPlanBudgeted',
        ),
    ]
