# Generated by Django 3.0.4 on 2020-05-09 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postfeed', '0035_auto_20200508_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
