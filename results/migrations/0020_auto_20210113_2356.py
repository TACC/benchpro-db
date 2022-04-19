# Generated by Django 3.1 on 2021-01-13 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0019_application_app_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='code',
        ),
        migrations.RemoveField(
            model_name='result',
            name='compiler',
        ),
        migrations.RemoveField(
            model_name='result',
            name='modules',
        ),
        migrations.RemoveField(
            model_name='result',
            name='mpi',
        ),
        migrations.RemoveField(
            model_name='result',
            name='version',
        ),
        migrations.AddField(
            model_name='application',
            name='build_label',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='module_use',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='username',
            field=models.CharField(default='mcawood', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='opt_flags',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]