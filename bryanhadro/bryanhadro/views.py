from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

from .models import WashingtonMetroAPI, AccuWeatherAPICountries, AccuWeatherAPIAdminAreas, AccuWeatherAPILocalConditions, AccuWeatherAPILocationTextSearching, AccuWeatherAPIGeoPositionSearching

def index(request):

    # station_codes = ["K07", "C04"] # Foggy Bottom and Dunn Loring.
    # data = WashingtonMetroAPI.do_rail_prediction_request(station_codes)
    # trains = data.get("Trains", [])

    # print trains

    return render_to_response('index.html')

def frontpage(request):

    context = {}

    # wmata_api = WashingtonMetroAPI()
    # stations = ["Dunn Loring-Merrifield", "Foggy Bottom-GWU"] # Foggy Bottom and Dunn Loring.
    # data = wmata_api.do_rail_prediction_request(stations)
    # trains = data.get("Trains", [])

    # eastbound_trains = []
    # westbound_trains = []
    # for train in trains:
    #     if train.get("DestinationCode") == wmata_api.stations.get("Vienna/Fairfax-GMU", {}).get("code"):
    #         westbound_trains.append(train)
    #     if train.get("DestinationCode") == wmata_api.stations.get("New Carrollton", {}).get("code"):
    #         eastbound_trains.append(train)
    # context["eastbound_trains"] = eastbound_trains
    # context["westbound_trains"] = westbound_trains

    # countries = AccuWeatherAPICountries("NAM").do_api_get()
    # areas = AccuWeatherAPIAdminAreas("US").do_api_get()
    # data = AccuWeatherAPIGeoPositionSearching().do_api_get()
    # data = AccuWeatherAPILocalConditions().do_api_get()
    # print data

    # foo = AccuWeatherAPILocalConditions().do_api_get()
    # print foo

    return render_to_response('frontpage/index.html', context)
