# Generated by Django 3.1 on 2021-03-10 15:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NotamArchive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=255)),
                ('aviation', models.CharField(max_length=255)),
                ('motorola', models.CharField(max_length=255)),
                ('notes', models.CharField(max_length=1000)),
                ('date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'notam_archive',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Notam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=255)),
                ('aviation', models.CharField(max_length=255)),
                ('motorola', models.CharField(max_length=255)),
                ('notes', models.CharField(max_length=1000)),
                ('date', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'notam',
                'managed': True,
            },
        ),
    ]
