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

            map = make_map_with_filter_opt(request.POST)
    else:
        map = map = folium.Map(location=[37.296933, -121.9574983], zoom_start=8,
                               height='100%', width='100%')._repr_html_()  # sample map

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
    map = folium.Map(location=[37.296933, -121.9574983], zoom_start=8,
                     height='70%', width='100%')
    folium.Marker(location=[37.4074687, -122.086669], popup="Google HQ", icon=folium.Icon(color='gray')).add_to(map)

    map = map._repr_html_()
    context = {'map': map}
    return render(request, 'main/map.html', context)


def make_map_with_filter_opt(post_data):
    COLORS = {'s_mount': 'blue'}
    map = folium.Map(location=[50.296933, 40.9574983], zoom_start=2,
                     height='100%', width='100%')

    activities = Activity.objects.all()  # change to 'find'
    for el in activities:
        print(post_data)
        if (el.type == post_data['type']) and (int(post_data['user_skill']) >= el.user_skill) and (
                el.enviroment_chars == int(post_data['enviroment_chars'])) and el.extreme == int(post_data['extreme']):
            location = [float(el.coords.split(',')[0]), float(el.coords.split(',')[1])]
            folium.Marker(location=location, popup=el.title, icon=folium.Icon(color=COLORS[el.type])).add_to(map)
        else:
            pass
    map = map._repr_html_()

    return map
