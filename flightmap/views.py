from django.shortcuts import render
from django.http import JsonResponse
from flightmap.get_openskydata_service.get_opensky_data import get_data


def index(request):
    return render(request, 'flightmap/index.html')


def flightdata(request):
    return JsonResponse(get_data())
