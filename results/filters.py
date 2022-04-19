import django_filters as filters
from django import forms
from .models import Result 
from .models import Application

class ResultFilter(filters.FilterSet):

    username =  filters.CharFilter(lookup_expr='icontains',label='Owner')
    system =    filters.CharFilter(lookup_expr='icontains',label='System')
    task_id =   filters.CharFilter(lookup_expr='icontains',label='Task ID')
    dataset =   filters.CharFilter(lookup_expr='icontains',label='Dataset')

    class Meta:
        model = Result
        fields = ['username', 'system', 'task_id', 'submit_time', 'dataset']

class AppFilter(filters.FilterSet):

    app_id =    filters.CharFilter(lookup_expr='icontains',label='Application')
    username =  filters.CharFilter(lookup_expr='icontains',label='Owner')
    system =    filters.CharFilter(lookup_expr='icontains',label='System')
    code =      filters.CharFilter(lookup_expr='icontains',label='Code')
    version =   filters.CharFilter(lookup_expr='icontains',label='Version')
    task_id =   filters.CharFilter(lookup_expr='icontains',label='Task ID')

    #start_time = filters.DateFilter(field_name="submit_time", lookup_expr='gte', label='Search date')
    #end_time = filters.DateFilter(field_name="submit_time", lookup_expr='lte', label='Search date')

    class Meta:
        model = Application
        fields = ['app_id', 'username', 'system',  'code', 'version', 'task_id']

