from rest_framework import (exceptions, serializers)
from core.models import *

class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = "__all__"