from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

from .models import WashingtonMetroAPI, AccuWeatherAPICountries, AccuWeatherAPIAdminAreas

def index(request):

    # station_codes = ["K07", "C04"] # Foggy Bottom and Dunn Loring.
    # data = WashingtonMetroAPI.do_rail_prediction_request(station_codes)
    # trains = data.get("Trains", [])

    # print trains

    return render_to_response('index.html')

def frontpage(request):

    station_codes = ["K07", "C04"] # Foggy Bottom and Dunn Loring.
    data = WashingtonMetroAPI.do_rail_prediction_request(station_codes)
    trains = data.get("Trains", [])

    # countries = AccuWeatherAPICountries("NAM").do_api_get()
    areas = AccuWeatherAPIAdminAreas("US").do_api_get()

    context = {
        "trains": trains,
        "areas": areas,
    }

    return render_to_response('frontpage/index.html', context)
