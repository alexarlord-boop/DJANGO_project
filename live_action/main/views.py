from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import FilterForm
from .models import Activity


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            # действия с данными фильтра
            return HttpResponseRedirect('/map')

    form = FilterForm()
    context = {
        'form': form
    }
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')


def goals(request):
    return render(request, 'main/goals.html')


def map(request):
    return render(request, 'main/map.html')
