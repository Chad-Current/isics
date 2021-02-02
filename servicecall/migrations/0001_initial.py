# Generated by Django 3.1 on 2021-01-24 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticketno', models.CharField(max_length=25)),
                ('site_loc', models.CharField(max_length=50)),
                ('issue', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
            ],
            options={
                'db_table': 'ticketlog',
                'managed': True,
            },
        ),
    ]
