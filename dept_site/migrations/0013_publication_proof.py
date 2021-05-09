# Generated by Django 3.2 on 2021-05-03 14:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dept_site', '0012_auto_20210503_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='proof',
            field=models.FileField(default=None, upload_to='proofs/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'ppt', 'word', 'txt'])]),
            preserve_default=False,
        ),
    ]