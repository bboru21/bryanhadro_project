from __future__ import unicode_literals

from django.db import models

import json
import urllib
import urllib2

class WashingtonMetroAPI():
    primary_key = "457d9ea8d5464cb9b29cadcd8e44a4b8"
    secondary_key = "1fe0a3391c5a48f6a31b7198d2712831"
    stations = {
        "All": {"code": "All"},
        "Dunn Loring-Merrifield": {"code": "K07"},
        "Foggy Bottom-GWU": {"code": "C04"},
        "Franconia-Springfield": {"code": "J03"},
        "Largo Town Center": {"code": "G05"},
        "New Carrollton": {"code": "D13"},
        "Vienna/Fairfax-GMU": {"code": "K08"},
        "Wiehle-Reston East": {"code": "N06"},
    }

    @classmethod
    def do_rail_prediction_request(cls, station_names=["All"]):

        json_response = {}

        station_codes = []
        for name in station_names:
            code = cls.stations.get(name, {}).get("code")
            if code:
                station_codes.append(code)

        url = "https://api.wmata.com/StationPrediction.svc/json/GetPrediction/%s?api_key=%s" % (','.join(station_codes), cls.primary_key)

        try:
            response = urllib2.urlopen(url, timeout=1).read()
            json_response = json.loads(response)
        except:
            pass

        return json_response

class AccuWeatherAPI():
    api_key = "hzJgpUoCxVuORDBk1MFSNRnnT8jopbAq"
    endpoint = ""

    @classmethod
    def do_api_get(cls):
        json_response = {}

        try:
            response = urllib2.urlopen(cls.endpoint, timeout=1).read()
            json_response = json.loads(response)
        except:
            pass

        return json_response

class AccuWeatherAPICountries(AccuWeatherAPI):

    @classmethod
    def __init__(cls, region_code):
        cls.endpoint = "http://dataservice.accuweather.com/locations/v1/countries/%s?apikey=%s" % (region_code, cls.api_key)

class AccuWeatherAPIAdminAreas(AccuWeatherAPI):

    @classmethod
    def __init__(cls, country_code):
        cls.endpoint = "http://dataservice.accuweather.com/locations/v1/adminareas/%s?apikey=%s" % (country_code, cls.api_key)

