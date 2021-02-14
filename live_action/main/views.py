from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h3>HELLO WORLD</h3>")


def about(request):
    return HttpResponse("<h3>About</h3>")
