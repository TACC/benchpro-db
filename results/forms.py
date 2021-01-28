from django import forms
from .models import Result, Application

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
			'gpus',
			'dataset',
			'result',
			'result_unit',
			'resource_path',
			'app_id'
		]

class AppForm(forms.ModelForm):
	class Meta:
		model = Application
		fields = [
			'username',
			'system',
			'code',
			'version',
			'build_label',
			'compiler',
			'mpi',
			'module_use',
			'modules',
			'opt_flags',
			'exe_file',
			'build_prefix',
			'build_date',
			'jobid',
			'app_id'
		]


