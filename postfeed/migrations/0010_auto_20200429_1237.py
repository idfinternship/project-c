# Generated by Django 3.0.5 on 2020-04-29 09:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('postfeed', '0009_auto_20200429_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 29, 9, 37, 4, 662429, tzinfo=utc)),
        ),
    ]
