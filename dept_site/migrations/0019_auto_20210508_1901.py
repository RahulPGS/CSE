# Generated by Django 3.2 on 2021-05-08 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dept_site', '0018_auto_20210508_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='award',
            name='date',
        ),
        migrations.RemoveField(
            model_name='events',
            name='date',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='date',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='date',
        ),
        migrations.RemoveField(
            model_name='news',
            name='date',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='date',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='date',
        ),
        migrations.AddField(
            model_name='award',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='award',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='events',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='events',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='faculty',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='faculty',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='gallery',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gallery',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='news',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publication',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
