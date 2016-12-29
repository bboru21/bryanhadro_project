from __future__ import unicode_literals

from django.db import models

import json
import urllib
import urllib2

class TwitterAPI():
    api_key = "bwtwrNwDg1tIMK9mlwmLUBlE1"

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
    version = "v1"

    @classmethod
    def do_api_get(cls):
        json_response = {}

        print cls.endpoint

        try:
            response = urllib2.urlopen(cls.endpoint, timeout=1).read()
            json_response = json.loads(response)
            # raw_data = urllib.urlopen(cls.endpoint).read()
            # json_data = json.loads(raw_data)
        except:
            pass

        return json_response

class AccuWeatherAPICountries(AccuWeatherAPI):

    @classmethod
    def __init__(cls, region_code):
        cls.endpoint = "http://dataservice.accuweather.com/locations/%s/countries/%s?apikey=%s" % (cls.version, region_code, cls.api_key)

class AccuWeatherAPIAdminAreas(AccuWeatherAPI):
    @classmethod
    def __init__(cls, country_code):
        cls.endpoint = "http://dataservice.accuweather.com/locations/%s/adminareas/%s?apikey=%s" % (cls.version, country_code, cls.api_key)

class AccuWeatherAPILocalConditions(AccuWeatherAPI):
    @classmethod
    def __init__(cls, location_key="2110938"):
        cls.endpoint = "http://dataservice.accuweather.com/locations/%s/cities/US/search.json?q=%s&apikey=%s&alias=always" % (cls.version, location_key, cls.api_key)

class AccuWeatherAPILocationTextSearching(AccuWeatherAPI):
    @classmethod
    def __init__(cls, country_code="US", search_text=""):
        cls.endpoint = "http://api.accuweather.com/locations/%s/%s/search.json?q=%s&apikey=%s&language=en" % (cls.version, country_code, search_text, cls.api_key)

class AccuWeatherAPIGeoPositionSearching(AccuWeatherAPI):
    @classmethod
    def __init__(cls, latitude="38.8856732", longitude="-77.23262319999999"):
        coordinates = "%s, %s" % (latitude, longitude)
        query = urllib.urlencode({'q': coordinates})
        cls.endpoint = "http://dataservice.accuweather.com/locations/%s/cities/geoposition/search.json?%s&apikey=%s&language=en" % (cls.version, query, cls.api_key)

'''
{u'SupplementalAdminAreas': [{u'EnglishName': u'Fairfax', u'LocalizedName': u'Fairfax', u'Level': 2}], u'DataSets': [], u'Country': {u'EnglishName': u'United States', u'ID': u'US', u'LocalizedName': u'United States'}, u'Region': {u'EnglishName': u'North America', u'ID': u'NAM', u'LocalizedName': u'North America'}, u'IsAlias': False, u'Rank': 75, u'LocalizedName': u'Dunn Loring', u'Version': 1, u'PrimaryPostalCode': u'22027', u'Key': u'2110938', u'TimeZone': {u'IsDaylightSaving': False, u'Code': u'EST', u'GmtOffset': -5.0, u'Name': u'America/New_York', u'NextOffsetChange': u'2017-03-12T07:00:00Z'}, u'EnglishName': u'Dunn Loring', u'AdministrativeArea': {u'LocalizedType': u'State', u'EnglishType': u'State', u'CountryID': u'US', u'Level': 1, u'LocalizedName': u'Virginia', u'EnglishName': u'Virginia', u'ID': u'VA'}, u'Type': u'City', u'GeoPosition': {u'Latitude': 38.893, u'Elevation': {u'Metric': {u'UnitType': 5, u'Unit': u'm', u'Value': 151.0}, u'Imperial': {u'UnitType': 0, u'Unit': u'ft', u'Value': 495.0}}, u'Longitude': -77.222}}
'''

