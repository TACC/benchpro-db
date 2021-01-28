import django_filters as filters
from django import forms
from .models import Result 
from .models import Application

class ResultFilter(filters.FilterSet):

	username = 	filters.CharFilter(lookup_expr='icontains',label='Username')
	system = 	filters.CharFilter(lookup_expr='icontains',label='System')
	jobid = 	filters.CharFilter(lookup_expr='icontains',label='JobID')
	app_id = 	filters.CharFilter(lookup_expr='icontains',label='Application')

	class Meta:
		model = Result
		fields = ['username', 'system', 'jobid', 'submit_time', 'app_id']

class AppFilter(filters.FilterSet):

	code = 		filters.CharFilter(lookup_expr='icontains',label='Code')
	version =	filters.CharFilter(lookup_expr='icontains',label='Version')
	system = 	filters.CharFilter(lookup_expr='icontains',label='System')
	jobid = 	filters.CharFilter(lookup_expr='icontains',label='JobID')
	app_id =    filters.CharFilter(lookup_expr='icontains',label='Application')

	#start_time = filters.DateFilter(field_name="submit_time", lookup_expr='gte', label='Search date')
	#end_time = filters.DateFilter(field_name="submit_time", lookup_expr='lte', label='Search date')

	class Meta:
		model = Application
		fields = ['code', 'version', 'system', 'jobid', 'app_id']

