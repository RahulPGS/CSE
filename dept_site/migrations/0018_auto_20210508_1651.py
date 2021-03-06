# Generated by Django 3.2 on 2021-05-08 11:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dept_site', '0017_auto_20210506_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='award',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='events',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='faculty',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='gallery',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='news',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='publication',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='staff',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='edu_level',
            field=models.CharField(choices=[('b_tech', 'B.Tech'), ('m_tech', 'M.Tech'), ('phd', 'PHD'), ('other', '(Other)')], max_length=50),
        ),
    ]
