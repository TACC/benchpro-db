from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ResultForm
from .models import Result

# Create your views here.


def home_view(request, *args, **kwargs):
    my_context = {
        "page_title": "Home Page",
        "my_list": [123, 456, 789]
    }

    return render(request, "home.html", my_context)

def result_create_view(request):
    form = ResultForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ResultForm()

    context = {
        'form': form
    }
    return render(request, "results/result_create.html", context)

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
    return render(request, "results/result_delete.html", context)

def result_list_view(request):
    queryset = Result.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "results/result_list.html", context)

def result_detail_view(request, id):
    obj = get_object_or_404(Result, id=id)
    context = {
        'object': obj
    }
    return render(request, "results/result_detail.html", context)

