from django.db import models

from utils.models import StampedModel


class Client (StampedModel):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name
