# Generated by Django 3.0.4 on 2020-04-01 15:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=200)),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2020, 4, 1, 15, 51, 9, 383158, tzinfo=utc))),
            ],
        ),
    ]
