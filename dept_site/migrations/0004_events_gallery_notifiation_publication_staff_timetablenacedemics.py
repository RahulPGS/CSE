# Generated by Django 3.1.7 on 2021-04-08 17:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dept_site', '0003_auto_20210404_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('res_person', models.CharField(max_length=100)),
                ('covinor', models.CharField(max_length=100)),
                ('coordinators', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='faculty_images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg', 'img'])])),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('Workshops', 'Workshops'), ('Talks', 'Talks'), ('Events', 'Events')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Notifiation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notifiation', models.CharField(max_length=500)),
                ('category', models.CharField(choices=[('announcements', 'Announcements'), ('updates', 'Updates'), ('placement drives', 'Placement drives')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('id_no', models.CharField(max_length=7)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('link', models.CharField(max_length=1000)),
                ('is_p', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('profession', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Timetablenacedemics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=1000)),
            ],
        ),
    ]
