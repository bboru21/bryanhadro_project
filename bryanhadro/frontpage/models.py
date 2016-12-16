from __future__ import unicode_literals

from django.db import models

import json
import urllib
import urllib2

class WashingtonMetroAPI():
    primary_key = "457d9ea8d5464cb9b29cadcd8e44a4b8"
    secondary_key = "1fe0a3391c5a48f6a31b7198d2712831"

    @classmethod
    def do_rail_prediction_request(cls, station_codes=["All"]):

        json_response = {}

        url = "https://api.wmata.com/StationPrediction.svc/json/GetPrediction/%s?api_key=%s" % (','.join(station_codes), cls.primary_key)

        try:
            response = urllib2.urlopen(url, timeout=1).read()
            json_response = json.loads(response)
        except:
            pass

        return json_response
