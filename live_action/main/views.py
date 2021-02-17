from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import FilterForm
from .models import Activity
import folium


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = FilterForm(request.POST)  # получаем данные из формы -> запрос к бд
        if form.is_valid():
            # действия с данными фильтра
            return HttpResponseRedirect('/map')

    form = FilterForm()

    map = folium.Map(location=[37.296933, -121.9574983], zoom_start=8,
                     height='100%', width='100%')
    folium.Marker(location=[37.4074687, -122.086669], popup="Google HQ", icon=folium.Icon(color='gray')).add_to(map)
    map = map._repr_html_()

    context = {
        'form': form,
        'map': map,
    }

    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')


def goals(request):
    return render(request, 'main/goals.html')


def map(request):
    map = folium.Map(location=[37.296933, -121.9574983], zoom_start=8,
                     height='70%', width='100%')
    folium.Marker(location=[37.4074687, -122.086669], popup="Google HQ", icon=folium.Icon(color='gray')).add_to(map)

    map = map._repr_html_()
    context = {'map': map}
    return render(request, 'main/map.html', context)
