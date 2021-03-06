# Generated by Django 3.2 on 2021-05-08 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dept_site', '0020_auto_20210508_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_year', models.CharField(max_length=4)),
                ('batch_link', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='link',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='award',
            name='link',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='link',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='timetablenacedemics',
            name='link',
            field=models.TextField(),
        ),
    ]
