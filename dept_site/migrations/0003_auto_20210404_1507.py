# Generated by Django 3.1.7 on 2021-04-04 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dept_site', '0002_auto_20210404_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='conf_attended',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='projects',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='publication',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='work_exp',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='workshops_attended',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
