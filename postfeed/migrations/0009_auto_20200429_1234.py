# Generated by Django 3.0.5 on 2020-04-29 09:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('postfeed', '0008_auto_20200416_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 29, 9, 34, 5, 464937, tzinfo=utc)),
        ),
    ]
