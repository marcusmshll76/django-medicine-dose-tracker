# Generated by Django 4.0.6 on 2022-07-27 13:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
