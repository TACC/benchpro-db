from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

from .forms import ResultForm
from .models import Result
from .filters import ResultFilter

# Create your views here.

def result_create_view(request):
	form = ResultForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ResultForm()

	context = {
		'form': form
	}
	return render(request, "result_create.html", context)

def result_delete_view(request, id):
	obj = get_object_or_404(Result, id=id)
	print(request.method)
	if request.method == 'POST':
		print("POST done")
		obj.delete()
		return redirect('/')
	context = {
		'object': obj
	}
	return render(request, "result_delete.html", context)

class result_list_view(ListView):
	queryset = Result.objects.all()
#	context_object_name = 'results'
#	paginate_by = 10
	template_name = 'result_list.html'
	ordering = ['submit_time']

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['filter'] = ResultFilter(self.request.GET, queryset=self.get_queryset())
		context['count'] = self.get_queryset().count()
		return context

def result_detail_view(request, id):
	obj = get_object_or_404(Result, id=id)
	context = {
		'object': obj
	}
	return render(request, "result_detail.html", context)

def test_view(request):
	queryset = Result.objects.all()
	context = {
	"object_list": queryset
	}
	return render(request, "test.html", context)

