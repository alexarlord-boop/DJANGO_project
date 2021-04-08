from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user
from .forms import FilterForm, GoalForm
from .models import Activity, Goal
from .activities import all_activities
import folium
from datetime import datetime

colors = {'s_mount': 'lightblue', 'under_water': 'blue', 'on_water': 'red'}


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


def add_goals(request, id):
    # base_map = folium.Map(location=[37.296933, -121.9574983], zoom_start=8,
    #                       height='100%', width='100%')._repr_html_()
    form = GoalForm()
    map, point = set_point(id)
    message = ''
    is_added = False
    if request.method == 'POST':

        if is_goal_in_list(point.title):
            message = f'{point.title} уже в ваших целях.'
        else:
            # добавление в модель цели
            add_goal_to_db(activity=point, user=get_user(request), data=get_data())
            message = f'{point.title} добавлено в цели.'
            is_added = True
        # print(message)

    context = {
        'form': form,
        'message': message,
        'is_added': is_added,
        'point': point,
        'map': map,
    }

    return render(request, 'main/add_goal.html', context)
    # return redirect('/')


def about(request):
    return render(request, 'main/about.html')


def goals(request, id=None, delete=None, status=None):
    curr_user = get_user(request)
    print(type(curr_user))
    if str(curr_user) == 'AnonymousUser':
        context = None
    else:
        user_goals = Goal.objects.filter(user__exact=get_user(request))

        description = None
        if id is not None:
            description = Goal.objects.filter(id__exact=id)[0]
        if status is not None:
            if status != -1:
                change_goal_status(id, status)

        if delete == 'delete':
            delete_goal(id)

        context = {
            'goals': user_goals,
            'descr': description,
        }

    return render(request, 'main/goals.html', context)


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


def goal_addition(id):
    pass


def set_point(id):
    point = Activity.objects.filter(id__exact=id)[0]
    location = [float(point.coords.split(',')[0]), float(point.coords.split(',')[1])]
    base_map = folium.Map(location=location, zoom_start=5,
                          height='100%', width='100%')

    folium.Marker(location=location, popup=point.title, icon=folium.Icon(color=colors[point.type])).add_to(base_map)
    point_on_map = base_map._repr_html_()
    return point_on_map, point


def make_map_with_filter_options(post_data):
    base_map = folium.Map(location=[50.296933, 40.9574983], zoom_start=2,
                          height='100%', width='100%')
    average_x, average_y = 0, 0
    # add_activities_to_db(all_activities)
    activities = Activity.objects.filter(type__exact=post_data['type'],
                                         season__exact=post_data['season'],
                                         enviroment_chars__exact=post_data['enviroment_chars'],
                                         extreme__lte=post_data['extreme'])

    for el in activities:
        location = [float(el.coords.split(',')[0]), float(el.coords.split(',')[1])]
        average_x = (average_x + location[0])
        average_y = (average_y + location[1])
        folium.Marker(location=location, popup=el.title, icon=folium.Icon(color=colors[el.type])).add_to(base_map)
    k = len(activities)
    if k != 0:
        base_map.location = [average_x / k, average_y / k]

    filter_map = base_map._repr_html_()

    return filter_map, activities


def add_activities_to_db(list_of_activities):
    for act in list_of_activities:
        new_activity = Activity(title=act['title'], description=act['description'],
                                coords=act['coords'], type=act['type'],
                                season=act['season'], enviroment_chars=act['enviroment_chars'],
                                extreme=act['extreme'])
        new_activity.save()


def add_one_activity_to_db(activitiy):
    new_activity = Activity(title=activitiy['title'], description=activitiy['description'],
                            coords=activitiy['coords'], type=activitiy['type'],
                            season=activitiy['season'], enviroment_chars=activitiy['enviroment_chars'],
                            extreme=activitiy['extreme'])
    new_activity.save()


def add_goal_to_db(activity, user, data):
    new_goal = Goal(activity=activity, user=user, title=activity.title,
                    add_data=data, is_done=0)
    new_goal.save()
    # print(new_goal.activity)


def is_goal_in_list(goal_title):
    goals = Goal.objects.filter(title__exact=goal_title)
    return len(goals) != 0


def change_goal_status(id, status):
    goal = Goal.objects.filter(id__exact=id)[0]
    goal.is_done = status
    goal.save()


def delete_goal(id):
    Goal.objects.filter(id__exact=id).delete()


def get_data():
    return datetime.today().strftime('%Y-%m-%d')


if __name__ == '__main__':
    add_activities_to_db(all_activities)
