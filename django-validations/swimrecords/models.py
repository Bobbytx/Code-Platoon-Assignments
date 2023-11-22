from django.db import models
from .validators import validate_stroke, validate_distance

class SwimRecord(models.Model):
    first_name = models.CharField(null=False, blank=False, max_length=50)
    last_name = models.CharField(null=False, blank=False, max_length=50)
    team_name = models.CharField(null=False, blank=False, max_length=100)
    relay = models.BooleanField(null=False, blank=False)
    stroke = models.CharField(null=False, blank=False, max_length=50, validators=[validate_stroke])
    distance = models.IntegerField(null=False, validators=[validate_distance])
    record_date = models.DateTimeField(null=False)
    record_broken_date = models.DateTimeField(null=False)
