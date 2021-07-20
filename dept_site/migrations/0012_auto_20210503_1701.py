# Generated by Django 3.2 on 2021-05-03 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dept_site', '0011_rename_categories_news_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.CharField(choices=[('Announcement', 'Announcement'), ('Update', 'Update'), ('Placement drive', 'Placement drive')], max_length=20),
        ),
    ]
