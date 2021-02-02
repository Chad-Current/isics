# Generated by Django 3.1 on 2021-01-23 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IsicApplicant',
            fields=[
                ('primary_key', models.BigIntegerField(primary_key=True, serialize=False)),
                ('applicant', models.CharField(max_length=255)),
                ('loi', models.BooleanField(default=False)),
                ('moa', models.BooleanField(default=False)),
                ('part_pl', models.BooleanField(default=False)),
                ('ugc', models.BooleanField(default=False)),
                ('isicsb_approved', models.BooleanField(default=False)),
                ('user_level', models.SmallIntegerField(default=1)),
            ],
            options={
                'db_table': 'applicants',
                'managed': False,
            },
        ),
    ]
