# Generated by Django 3.0.5 on 2020-04-29 16:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('postfeed', '0020_auto_20200429_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 29, 16, 44, 39, 100500, tzinfo=utc)),
        ),
    ]
