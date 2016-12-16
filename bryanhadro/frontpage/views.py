from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import WashingtonMetroAPI

def index(request):

    station_codes = ["K07", "C04"] # Foggy Bottom and Dunn Loring.
    data = WashingtonMetroAPI.do_rail_prediction_request(station_codes)
    trains = data.get("Trains", [])

    print trains

    template = loader.get_template('frontpage/index.html')
    context = {
        "trains": trains
    }


    return HttpResponse(True)
    # return HttpResponse(template.render(context, request))
