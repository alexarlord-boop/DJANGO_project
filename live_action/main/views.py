from django.shortcuts import render
from .models import Activity

# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def goals(request):
    return render(request, 'main/goals.html')


def map(request):
    return render(request, 'main/map.html')

