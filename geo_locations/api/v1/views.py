# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import requests
from collections import OrderedDict

from core.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException

from .serializers import *


def create_response(response_data):
    """
    method used to create response data in given format
    """
    response = OrderedDict()
    response["header"] = {"status": "1"}
    response["body"] = response_data
    return response


def create_error_response(response_data):
    """
    method used to create response data in given format
    """
    return OrderedDict({"header": {"status": "0"},"errors": response_data})


class WeatherAPI(APIView):
    def get(self, request):
        serializer = WeatherSerializer(Location.objects.filter(state=request.data.get("state")).first(), many=False)
        all_details = serializer.data
        url = "https://api.weather.gov/points/{0},{1}".format(serializer.data.get('latitude'),serializer.data.get('longitude'))
        response = requests.get(url, headers={"content-type":"text"})
        if response.status_code != 200:
            return Response(create_error_response({"Msg":"ERROR"}), status=response.status_code)
        response = response.json()
        forecast_url = response["properties"]["forecast"]
        forecast_response = requests.get(forecast_url)
        if forecast_response.status_code != 200:
            return Response(create_error_response({"Msg":"ERROR"}), status=response.status_code)
        forecast_response = forecast_response.json()["properties"]["periods"]
        weather_details = []
        for row in forecast_response:
            weather_details.append({"day":row["name"],
                                    "start_time":row["startTime"],
                                    "end_time":row["endTime"],
                                    "temperature":str(row["temperature"]) + row["temperatureUnit"],
                                    "wind_speed":row["windSpeed"],
                                    "wind_direction":row["windDirection"],
                                    "short_forecast":row["shortForecast"],
                                    "detailed_forecast":row["detailedForecast"]})

        all_details["weather"] =weather_details                                    
        return Response(create_response({"weather_details": all_details}))

