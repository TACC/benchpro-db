from django.db import models
from django.utils.timezone import now

# Create your models here.

# Base job class
class Job(models.Model):
    username            = models.CharField(max_length=50, blank=False)
    system              = models.CharField(max_length=50, blank=False)
    submit_time         = models.DateTimeField(blank=False)
    elapsed_time        = models.IntegerField(default=0, blank=True, null=True)
    end_time            = models.DateTimeField(default=now, blank=True, null=True)
    task_id             = models.CharField(max_length=50, blank=False, primary_key=True) 

    class Meta:
        abstract = True

# Holds application build info
class Application(Job):
    code                = models.CharField(max_length=50, blank=False)
    version             = models.CharField(max_length=50, blank=False)
    build_label         = models.CharField(max_length=50, blank=True, null=True)
    compiler            = models.CharField(max_length=50, blank=False)
    mpi                 = models.CharField(max_length=50, blank=False)
    module_use          = models.CharField(max_length=100, blank=True, null=True)
    modules             = models.CharField(max_length=200, blank=False)
    opt_flags           = models.CharField(max_length=200, blank=True, null=True)
    bin_dir             = models.CharField(max_length=50, blank=True, null=True)
    exe_file            = models.CharField(max_length=50, blank=False)
    build_prefix        = models.CharField(max_length=200, blank=False)
    script              = models.CharField(max_length=50, blank=True, null=True)
    exec_mode           = models.CharField(max_length=100, blank=False)
    app_id              = models.CharField(max_length=50, blank=False, unique=True)
    stdout              = models.CharField(max_length=50, blank=False)
    stderr              = models.CharField(max_length=50, blank=False)

    def get_absolute_url(self):
        return f"/app/{self.task_id}/"

# Hold benchmark result info
class Result(Job):
    capture_time        = models.DateTimeField(default=now, blank=True)
    description         = models.CharField(max_length=100, blank=True)
    exec_mode           = models.CharField(max_length=100, blank=False)
    job_status          = models.CharField(max_length=100, blank=False)
    nodelist            = models.CharField(max_length=1000, blank=False)
    nodes               = models.IntegerField(blank=False)
    ranks               = models.IntegerField(blank=False)
    threads             = models.IntegerField(blank=False, default=1)
    gpus                = models.IntegerField(blank=False, default=0)
    dataset             = models.CharField(max_length=50, blank=False)
    result              = models.DecimalField(decimal_places=3, max_digits=20, blank=False)
    result_unit         = models.CharField(max_length=50, blank=False)
    resource_path       = models.CharField(max_length=100, blank=True)
    app_id              = models.CharField(max_length=50, blank=False)

    def get_absolute_url(self):
        return f"/result/{self.task_id}/"
