# Generated by Django 3.1 on 2021-01-11 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0015_result_job_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('version', models.CharField(max_length=50)),
                ('system', models.CharField(max_length=50)),
                ('compiler', models.CharField(max_length=50)),
                ('mpi', models.CharField(max_length=50)),
                ('modules', models.CharField(max_length=50)),
                ('opt_flags', models.CharField(max_length=200)),
                ('exe_file', models.CharField(max_length=50)),
                ('build_prefix', models.CharField(max_length=50)),
                ('build_date', models.DateTimeField()),
                ('jobid', models.IntegerField()),
            ],
        ),
    ]
