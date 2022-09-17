from django.db import models
from model_clone.models import CloneModel


class StampedModel(CloneModel):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
