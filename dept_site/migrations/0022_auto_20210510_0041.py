# Generated by Django 3.2 on 2021-05-09 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dept_site', '0021_auto_20210508_2337'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='staff',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]