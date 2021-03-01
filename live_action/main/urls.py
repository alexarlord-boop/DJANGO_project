from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('map', views.map),
    path('goals', views.goals),
    path('about', views.about),
    path('add_goals/<int:activity_id/>', views.add_goals)
]