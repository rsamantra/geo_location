from django.views.generic import TemplateView
from django.shortcuts import render
from .models import *

# Create your views here.

class StateView(TemplateView):
    template_name = "initial.html"


class MapView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(MapView, self).get_context_data(**kwargs)
        state = self.request.GET.get("state")
        location_obj = Location.objects.filter(state=state).first()
        if location_obj:
            context["latitude"] = location_obj.latitude
            context["longitude"] = location_obj.longitude
        else:
            context["latitude"] = 0
            context["longitude"] = 0
        return context        