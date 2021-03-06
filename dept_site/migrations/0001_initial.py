# Generated by Django 3.1.7 on 2021-04-04 06:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('edu_level', models.CharField(choices=[('b_tech', 'B.Tech'), ('m_tech', 'M.Tech'), ('phd', 'PHD'), ('other', '(Other')], max_length=50)),
                ('education', models.CharField(max_length=500)),
                ('spec_sub', models.CharField(max_length=100)),
                ('work_exp', models.CharField(max_length=500)),
                ('publication', models.CharField(max_length=1000)),
                ('projects', models.CharField(max_length=1000)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('sub_dealt', models.CharField(max_length=500)),
                ('conf_attended', models.CharField(max_length=500)),
                ('workshops_attended', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='faculty_images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg', 'img'])])),
                ('cv', models.ImageField(upload_to='faculty_cv/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'txt', 'doc', 'jpg', 'png', 'jpeg', 'img'])])),
            ],
        ),
    ]
