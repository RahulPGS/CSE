# Generated by Django 3.2.3 on 2021-05-27 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dept_site', '0028_auto_20210519_1426'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
                ('a_file', models.FileField(blank=True, null=True, upload_to='')),
                ('f_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dept_site.news')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]