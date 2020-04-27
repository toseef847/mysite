from django.urls import path
from . import views

app_name = 'subjects'
urlpatterns = [
    path('', views.index, name='index'),
    path('newclass', views.newclass, name='newclass'),
    path('classes', views.classes, name='classes'),
    path('newsubject', views.newsubject, name='newsubject'),
]
