# Generated by Django 3.1 on 2021-07-14 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriberTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('badge_identifier', models.CharField(max_length=25)),
                ('location', models.CharField(max_length=255)),
                ('talkgroup_assoc', models.CharField(max_length=255)),
                ('rssi', models.IntegerField(default=0)),
                ('mobile', models.BooleanField(default=False)),
                ('portable', models.BooleanField(default=False)),
                ('desc_issue', models.CharField(max_length=1500)),
                ('issue_resolved', models.BooleanField(blank=True)),
                ('desc_resolve', models.CharField(blank=True, max_length=1500)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'subscriber_tickets',
                'managed': True,
            },
        ),
    ]
