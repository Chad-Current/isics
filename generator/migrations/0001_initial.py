# Generated by Django 3.1 on 2021-01-29 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Generator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gen_location', models.CharField(max_length=255)),
                ('gen_address', models.CharField(max_length=255)),
                ('gen_cost', models.CharField(max_length=255)),
                ('gen_contract', models.CharField(max_length=50)),
                ('gen_vendor', models.CharField(max_length=50)),
                ('gen_poc', models.CharField(max_length=100)),
                ('gen_phonenumber', models.CharField(max_length=25)),
                ('gen_email', models.EmailField(max_length=255)),
            ],
            options={
                'db_table': 'generator',
                'managed': True,
            },
        ),
    ]
