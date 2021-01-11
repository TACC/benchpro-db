from django.db import models
from django.utils.timezone import now

# Create your models here.


class Result(models.Model):
	username 		= models.CharField(max_length=50, blank=False)
	system			= models.CharField(max_length=50, blank=False)
	submit_time 	= models.DateTimeField(blank=False)
	elapsed_time 	= models.IntegerField(default=0, blank=True, null=True)
	end_time 		= models.DateTimeField(default=now, blank=True, null=True)
	capture_time 	= models.DateTimeField(default=now, blank=True)
	description 	= models.CharField(max_length=100, blank=True)
	jobid 			= models.IntegerField(blank=False)
	job_status		= models.CharField(max_length=100, blank=False)
	nodelist 		= models.CharField(max_length=1000, blank=False)
	nodes 			= models.IntegerField(blank=False)
	ranks 			= models.IntegerField(blank=False)
	threads 		= models.IntegerField(blank=False, default=1)
	code 			= models.CharField(max_length=50, blank=False)
	version 		= models.CharField(max_length=50, blank=False)
	compiler 		= models.CharField(max_length=50, blank=True)
	mpi 			= models.CharField(max_length=50, blank=True)
	modules 		= models.CharField(max_length=200, blank=True)
	dataset 		= models.CharField(max_length=50, blank=False)
	result 			= models.DecimalField(decimal_places=3, max_digits=20, blank=False)
	result_unit 	= models.CharField(max_length=50, blank=False)

	resource_path 	= models.CharField(max_length=100, blank=True)

	def get_absolute_url(self):
		return f"/result/{self.id}/"
