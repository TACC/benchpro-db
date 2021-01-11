# Generated by Django 3.1 on 2021-01-11 13:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0008_result_capture_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='elapsed_time',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='result',
            name='end_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
