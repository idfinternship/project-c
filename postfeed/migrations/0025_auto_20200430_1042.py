# Generated by Django 3.0.5 on 2020-04-30 07:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('postfeed', '0024_auto_20200430_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 30, 7, 42, 41, 606643, tzinfo=utc)),
        ),
    ]