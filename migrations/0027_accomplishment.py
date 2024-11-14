# Generated by Django 5.0.7 on 2024-08-02 15:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rasmApp', '0026_apsummary_rename_bremark2_budgetedap_remark_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accomplishment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bapmonth', models.CharField(blank=True, choices=[('መስከረም', 'መስከረም'), ('ጥቅምት', 'ጥቅምት'), ('ህዳር', 'ህዳር'), ('ታህሳስ', 'ታህሳስ'), ('ጥር', 'ጥር'), ('የካቲት', 'የካቲት'), ('መጋቢት', 'መጋቢት'), ('ሚያዚያ', 'ሚያዚያ'), ('ግንቦት', 'ግንቦት'), ('ሰኔ', 'ሰኔ'), ('ሐምሌ', 'ሐምሌ'), ('ነሐሴ', 'ነሐሴ')], max_length=20, null=True)),
                ('actionInBr', models.FloatField(blank=True, default=None, null=True)),
                ('actionInKm', models.FloatField(blank=True, default=None, null=True)),
                ('bremark1', models.CharField(blank=True, choices=[('በጦርነቱ/በፀጥታ ችግር ምክንያት', 'በጦርነቱ/በፀጥታ ችግር ምክንያት'), ('በኮንትራት የሚተዳደሩ ፕሮጀክቶች በመቋረጣቸው ምክንያት', 'በኮንትራት የሚተዳደሩ ፕሮጀክቶች በመቋረጣቸው ምክንያት'), ('በግዢ ሂደት ላይ ያሉ ፕሮጀክቶች', 'በግዢ ሂደት ላይ ያሉ ፕሮጀክቶች'), ('በግብአት እጥረት ምክንያት', 'በግብአት እጥረት ምክንያት'), ('በመንገድ ወሰን ማስከበር ምክንያት', 'በመንገድ ወሰን ማስከበር ምክንያት'), ('የተለያየ (Others)', 'የተለያየ (Others)')], max_length=100, null=True)),
                ('bremark2', models.TextField(blank=True, default=None, null=True)),
                ('erabudget', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='rasmApp.erabudget')),
            ],
            options={
                'db_table': 'accomplishmentTb',
                'ordering': ['erabudget'],
            },
        ),
    ]
