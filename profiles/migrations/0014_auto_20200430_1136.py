# Generated by Django 3.0.5 on 2020-04-30 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_auto_20200430_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, default='', max_length=25, null=True),
        ),
    ]