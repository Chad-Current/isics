# Generated by Django 3.1 on 2021-03-04 21:41

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tower_cell', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=255)),
                ('sent_list', models.TextField(default='No record of email being sent')),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'email_record',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EmailTo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('county', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'email_list',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Sitemaintenance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tower_cell', models.CharField(max_length=255)),
                ('tower_assoc', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=2000), size=None)),
            ],
            options={
                'db_table': 'sitemaintenance',
                'managed': True,
            },
        ),
    ]
