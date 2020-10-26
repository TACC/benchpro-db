import django_filters as filters
from django import forms
from .models import Result 

class ResultFilter(filters.FilterSet):

	username = filters.CharFilter(lookup_expr='icontains',label='Username')
	system = filters.CharFilter(lookup_expr='icontains',label='System')
	jobid = filters.CharFilter(lookup_expr='icontains',label='JobID')
	#start_time = filters.DateFilter(field_name="submit_time", lookup_expr='gte', label='Search date')
	#end_time = filters.DateFilter(field_name="submit_time", lookup_expr='lte', label='Search date')
	code = filters.CharFilter(lookup_expr='icontains',label='Application')

	class Meta:
		model = Result
		fields = ['username', 'system', 'jobid', 'submit_time', 'code']
