from django.conf.urls import url, include
from .views import *

app_name = 'v1'

urlpatterns = [
    url(r'^get-weather/$', WeatherAPI.as_view(),name="get-weather"),
]