from django.db import models
from django.db.models import DO_NOTHING

from required_app.models import Engineer
from required_app.models.client import Client
from required_app.models.segment import Segment
from utils.models import StampedModel
from datetime import date


class RequiredProject(StampedModel):
    DEPARTMENTS = (
        ("LOW VOLTAGE", "LOW VOLTAGE"),
        ("MEDIUM VOLTAGE", "MEDIUM VOLTAGE"),
        ("MAINTENANCE", "MAINTENANCE"),
        ("STEEL", "STEEL")
    )
    REQUIRED = 1
    SUBMITTED = 2
    REVIEWED = 3
    PRODUCTION = 4
    STATUS = (
        (REQUIRED, "REQUIRED"),
        (SUBMITTED, "SUBMITTED"),
        (REVIEWED, "REVIEWED"),
        (PRODUCTION, "PRODUCTION")
    )
    required_number = models.IntegerField()
    year = models.IntegerField(default=date.today().year)
    client = models.ForeignKey(to=Client, on_delete=DO_NOTHING)
    project_name = models.CharField(max_length=100)
    consultant = models.CharField(max_length=100, blank=True, null=True)
    owner = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(choices=DEPARTMENTS, max_length=30)
    deadline = models.DateField(null=True, blank=True)
    comments = models.CharField(max_length=300, null=True, blank=True)
    sales_engineer = models.ManyToManyField(to=Engineer, related_name="sales_engineer")
    study_engineer = models.ManyToManyField(to=Engineer, related_name="study_engineer")
    required_date = models.DateField()
    amber = models.CharField(max_length=10, blank=True, null=True)
    sub_segment = models.ForeignKey(to=Segment, on_delete=DO_NOTHING)
    status = models.IntegerField(choices=STATUS, default=REQUIRED)
    is_deleted = models.BooleanField(default=False)

    @property
    def required_id(self):
        req_id = str(self.pk)
        while len(req_id) < 4:
            req_id = "0" + req_id
        return "{}/{}".format(req_id, self.year)

    @property
    def segment(self):
        # return "SEGMENT"
        s = Segment.objects.filter(id=self.sub_segment.id).last()
        return str(s.parent.name)

    def __str__(self):
        return "{} - {}".format(self.required_id, self.project_name)
