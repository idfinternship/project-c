# Generated by Django 3.0.5 on 2020-05-14 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postfeed', '0037_merge_20200513_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
