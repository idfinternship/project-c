# Generated by Django 3.0.4 on 2020-04-30 14:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('postfeed', '0032_auto_20200430_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 30, 14, 29, 4, 369589, tzinfo=utc)),
        ),
    ]
