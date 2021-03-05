from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('map', views.map),
    path('goals', views.goals),
    path('goals/<int:id>', views.goals),
    path('goals/<int:id>/<int:status>', views.goals),
    path('about', views.about),
    path('add_goal/<int:id>', views.add_goals)
]