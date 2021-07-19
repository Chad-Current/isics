# Generated by Django 3.1 on 2021-03-26 20:03

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
            name='ServiceTicketArchive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticketno', models.CharField(max_length=25, unique=True)),
                ('site_loc', models.CharField(max_length=50)),
                ('issue', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('user_serv', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'ticketlogarchive',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ServiceTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticketno', models.CharField(max_length=25, unique=True)),
                ('site_loc', models.CharField(max_length=50)),
                ('issue', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('user_serv', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'ticketlog',
                'managed': True,
            },
        ),
    ]
