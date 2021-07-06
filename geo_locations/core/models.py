from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Location(models.Model):
    state = models.CharField(max_length=200,unique=True)
    latitude = models.FloatField(validators=[MinValueValidator(-90), MaxValueValidator(90)])
    longitude = models.FloatField(validators=[MinValueValidator(-180), MaxValueValidator(180)])
