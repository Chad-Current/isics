# Generated by Django 3.1 on 2021-01-24 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(default='Unknown', max_length=255)),
                ('site_id', models.IntegerField()),
                ('site_asr', models.IntegerField()),
                ('site_location', models.CharField(default='Unknown', max_length=255)),
                ('state_owned', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'site',
                'managed': True,
            },
        ),
    ]
