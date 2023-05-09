from django.db import models
from Profile.models import ProfileData

class Filter(models.Model):
    profile_data = models.ForeignKey(ProfileData, on_delete = models.CASCADE, blank=True, null=True)
    age_limit_lower = models.IntegerField(default=18,  blank=True, null=True)
    age_limit_upper = models.IntegerField(default=100,  blank=True, null=True)

    height_limit_lower = models.IntegerField(default=140,  blank=True, null=True)
    height_limit_upper = models.IntegerField(default=220,  blank=True, null=True)

