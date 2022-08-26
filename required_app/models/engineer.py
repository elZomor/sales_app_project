from django.db import models

from utils.models import StampedModel


class Engineer(StampedModel):
    full_name = models.CharField(max_length=100, blank=False, null=False)
    initials = models.CharField(max_length=5, blank=False, null=False)
    profile_picture = models.FileField(upload_to="engineer-profile-picture", null=True, blank=True)

    def __str__(self):
        return self.full_name
