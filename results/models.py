from django.db import models
from django.utils.timezone import now

# Create your models here.


class Result(models.Model):
    user = models.CharField(max_length=50, blank=False)
    system = models.CharField(max_length=50, blank=False)
    submit_time = models.DateTimeField(default=now, blank=False)
    jobid = models.IntegerField(blank=False)
    nodes = models.IntegerField(blank=False)
    ranks = models.IntegerField(blank=False)
    threads = models.IntegerField(blank=False, default=1)
    code = models.CharField(max_length=50, blank=False)
    version = models.CharField(max_length=50, blank=False)
    compiler = models.CharField(max_length=50, blank=True)
    mpi = models.CharField(max_length=50, blank=True)
    modules = models.CharField(max_length=200, blank=True)
    dataset = models.CharField(max_length=50, blank=False)
    result = models.DecimalField(decimal_places=3, max_digits=20, blank=False)
    result_unit = models.CharField(max_length=50, blank=False)

    def get_absolute_url(self):
        return f"/result/{self.id}/"