# Generated by Django 3.1 on 2021-03-04 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alarm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=1000)),
                ('alarm', models.CharField(max_length=1000)),
                ('opened', models.CharField(max_length=1000)),
                ('ticket', models.CharField(max_length=255)),
                ('priority', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('notes', models.CharField(max_length=1000)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'alarm',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AlarmArchive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arcv_site_name', models.CharField(max_length=5000)),
                ('arcv_alarm', models.CharField(max_length=5000)),
                ('arcv_alarm_opened', models.CharField(max_length=5000)),
                ('all_comments', models.CharField(max_length=5000)),
                ('time_stamp', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'alarm_archive',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AlarmComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('comments', models.CharField(max_length=250)),
                ('original_alarm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alarm.alarm')),
            ],
            options={
                'db_table': 'alarmtrace',
                'managed': True,
            },
        ),
    ]
