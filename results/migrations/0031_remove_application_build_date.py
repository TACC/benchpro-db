# Generated by Django 3.2.12 on 2022-03-28 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0030_auto_20220318_1101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='build_date',
        ),
    ]