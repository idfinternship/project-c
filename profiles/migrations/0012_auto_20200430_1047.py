# Generated by Django 3.0.5 on 2020-04-30 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_auto_20200430_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='icon',
            field=models.ImageField(blank=True, upload_to='icons'),
        ),
    ]