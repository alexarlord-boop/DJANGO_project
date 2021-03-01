from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import FilterForm, GoalForm
from .models import Activity
from .activities import all_activities
import folium

colors = {'s_mount': 'lightblue', 'under_water': 'deepblue', 'on_water': 'red'}


# Create your views here.
def index(request):
    base_map = folium.Map(location=[37.296933, -121.9574983], zoom_start=8,
                          height='100%', width='100%')._repr_html_()

    form = FilterForm()
    points = list()
    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            base_map, points = make_map_with_filter_options(request.POST)

    context = {
        'form': form,
        'map': base_map,
        'points': points,
    }

    return render(request, 'main/index.html', context)


def add_goals(request):
    if request.method == 'POST':
        pass
    return render(request, 'main/add_goals.html', context)
    # return redirect('/')


def about(request):
    return render(request, 'main/about.html')


def goals(request):
    return render(request, 'main/goals.html')


def map(request):
    base_map = folium.Map(location=[40, 20],
                          zoom_start=2,
                          height='77%', width='100%')

    popup = folium.LatLngPopup()
    base_map.add_child(popup)

    activities = Activity.objects.all()
    for el in activities:
        location = [float(el.coords.split(',')[0]), float(el.coords.split(',')[1])]
        folium.Marker(location=location, popup=el.title, icon=folium.Icon(color=colors[el.type])).add_to(base_map)

    map = base_map._repr_html_()
    context = {'map': map}
    return render(request, 'main/map.html', context)


def make_map_with_filter_options(post_data):
    base_map = folium.Map(location=[50.296933, 40.9574983], zoom_start=2,
                          height='100%', width='100%')
    # add_activities_to_db(all_activities)
    activities = Activity.objects.filter(type__exact=post_data['type'],
                                         user_skill__lte=post_data['user_skill'],
                                         enviroment_chars__exact=post_data['enviroment_chars'],
                                         extreme__lte=post_data['extreme'])
    for el in activities:
        location = [float(el.coords.split(',')[0]), float(el.coords.split(',')[1])]
        folium.Marker(location=location, popup=el.title, icon=folium.Icon(color=colors[el.type])).add_to(base_map)

    filter_map = base_map._repr_html_()

    return filter_map, activities


def add_activities_to_db(list_of_activities):
    for act in list_of_activities:
        new_activity = Activity(title=act['title'], description=act['description'],
                                coords=act['coords'], type=act['type'],
                                user_skill=act['user_skill'], enviroment_chars=act['enviroment_chars'],
                                extreme=act['extreme'])
        new_activity.save()


def add_one_activity_to_db(activitiy):
    new_activity = Activity(title=activitiy['title'], description=activitiy['description'],
                            coords=activitiy['coords'], type=activitiy['type'],
                            user_skill=activitiy['user_skill'], enviroment_chars=activitiy['enviroment_chars'],
                            extreme=activitiy['extreme'])
    new_activity.save()


if __name__ == '__main__':
    add_activities_to_db(all_activities)
