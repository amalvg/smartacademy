# Generated by Django 3.1.4 on 2020-12-30 13:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registerapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='dob',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
