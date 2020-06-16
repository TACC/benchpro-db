from django import forms

from .models import Result

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = [
            'user',
            'system',
            'submit_time',
            'jobid',
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


class RawResultForm(forms.Form):
    jobid = forms.IntegerField(required=True)
    user = forms.CharField()
