from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import FilterForm
from .models import Activity
import folium

colors = {'s_mount': 'white', 'under_water': 'deep-blue', 'on_water': 'blue'}


# Create your views here.
def index(request):
    map = folium.Map(location=[37.296933, -121.9574983],
                     zoom_start=8,
                     height='100%',
                     width='100%')._repr_html_()  # base map

    if request.method == 'POST':
        form = FilterForm(request.POST)  # получаем данные из формы -> запрос к бд
        if form.is_valid():
            # действия с данными фильтра
            map = make_map_with_filter_options(request.POST)

    form = FilterForm()
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
    map = folium.Map(location=[37.296933, -121.9574983],
                     zoom_start=8,
                     height='70%', width='100%')

    map = map._repr_html_()
    context = {'map': map}
    return render(request, 'main/map.html', context)


def make_map_with_filter_options(post_data):
    base_map = folium.Map(location=[50.296933, 40.9574983], zoom_start=2,
                          height='100%', width='100%')

    activities = Activity.objects.filter(type__exact=post_data['type'],
                                         user_skill__lte=post_data['user_skill'],
                                         enviroment_chars__exact=post_data['enviroment_chars'],
                                         extreme__lte=post_data['extreme'])
    print(activities)
    for el in activities:
        location = [float(el.coords.split(',')[0]), float(el.coords.split(',')[1])]
        folium.Marker(location=location, popup=el.title, icon=folium.Icon(color=colors[el.type])).add_to(base_map)

    filter_map = base_map._repr_html_()

    return filter_map
