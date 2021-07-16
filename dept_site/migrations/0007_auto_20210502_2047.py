# Generated by Django 3.2 on 2021-05-02 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dept_site', '0006_auto_20210409_0047'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('categories', models.CharField(choices=[('announcements', 'Announcements'), ('updates', 'Updates'), ('placement drives', 'Placement drives')], max_length=20)),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
        migrations.AddField(
            model_name='events',
            name='description',
            field=models.TextField(default='  '),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='faculty',
            name='conf_attended',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='education',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='projects',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='work_exp',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='description',
            field=models.TextField(),
        ),
    ]
