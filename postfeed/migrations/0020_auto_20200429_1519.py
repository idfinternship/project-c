# Generated by Django 3.0.4 on 2020-04-29 12:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('postfeed', '0019_auto_20200429_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 29, 12, 19, 53, 449867, tzinfo=utc)),
        ),
    ]