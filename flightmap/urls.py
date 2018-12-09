from django.urls import path
from . import views

"""Url patterns for flightmap module"""
urlpatterns = [
    path('', views.index, name='index'),
    path('flightdata', views.flightdata, name='flightdata'),
]
