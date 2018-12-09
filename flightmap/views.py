from django.shortcuts import render
from django.http import JsonResponse
from flightmap.get_openskydata_service.get_opensky_data import get_data


def index(request):
    """
    Returns flight radar html view
    :param request: Http request
    :return: Html view
    """
    return render(request, 'flightmap/index.html')


def flightdata():
    """
    Returns opensky-net flight radar data
    :return:
    """
    return JsonResponse(get_data())
