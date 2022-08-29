from django.db import models

from utils.models import StampedModel


class Segment(StampedModel):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(to='self', null=True, blank=True, related_name="children", on_delete=models.CASCADE)

    def __str__(self):
        return self.parent.name + ": " + self.name if self.parent else self.name
    