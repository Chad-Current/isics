# Generated by Django 3.1 on 2021-07-14 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notam', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notamextend',
            name='original_notam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notam.notam'),
        ),
    ]
