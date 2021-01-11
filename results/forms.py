from django import forms
from .models import Result

class ResultForm(forms.ModelForm):
	class Meta:
		model = Result
		fields = [
			'username',
			'system',
			'submit_time',
			'elapsed_time',
			'end_time',
			'capture_time',
			'description',
			'jobid',
			'job_status',
			'nodelist',
			'nodes',
			'ranks',
			'threads',
			'code',
			'version',
			'compiler',
			'mpi',
			'modules',
			'dataset',
			'result',
			'result_unit'
		]


