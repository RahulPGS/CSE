# Generated by Django 3.1.7 on 2021-04-08 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dept_site', '0004_events_gallery_notifiation_publication_staff_timetablenacedemics'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetablenacedemics',
            name='is_time',
            field=models.BooleanField(default=True),
        ),
    ]