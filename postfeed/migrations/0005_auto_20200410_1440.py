# Generated by Django 3.0.5 on 2020-04-10 11:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('postfeed', '0004_auto_20200408_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 11, 40, 22, 970053, tzinfo=utc)),
        ),
    ]
