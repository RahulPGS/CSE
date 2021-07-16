# Generated by Django 3.2 on 2021-05-06 09:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dept_site', '0016_auto_20210504_2337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('id_no', models.CharField(max_length=7)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('link', models.CharField(blank=True, max_length=1000, null=True)),
                ('approved', models.BooleanField(default=False)),
                ('proof', models.FileField(upload_to='proofs/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'ppt', 'word', 'txt'])])),
            ],
        ),
        migrations.RemoveField(
            model_name='publication',
            name='is_p',
        ),
    ]
