from datetime import date

from django.db.models import CASCADE

from required_app.models import RequiredProject
from utils.models import StampedModel
from django.db import models


class SubmittedProject(StampedModel):
    STATUS = (
        ("WON", "Won"),
        ("LOST", "Lost"),
        ("CANCELLED", "Cancelled"),
        ("POSTPONED", "Postponed"),
        ("DELAYED", "Deployed"),
        ("PENDING", "Pending"),
        ("SUBMITTED", "Submitted")
    )
    REASONS = (
        ("AFTER_DATE", "After Date"),
        ("UNFOLLOWED", "Unfollowed"),
        ("OVER_PRICED", "Over Priced"),
        ("TECHNICALLY_REJECTED", "Technically Rejected"),
        ("OUT_OF_OUR_SCOPE", "Out Of Our Scope")
    )

    required_project = models.ForeignKey(to=RequiredProject, on_delete=CASCADE)
    submitted_number = models.IntegerField()
    year = models.IntegerField(default=date.today().year)
    reference = models.CharField(max_length=100)
    initial_price = models.FloatField()
    number_of_items = models.IntegerField()
    submission_date = models.DateField(default=date.today())
    offer_status = models.CharField(choices=STATUS, default="SUBMITTED", max_length=30)
    rejection_reasons = models.CharField(choices=REASONS, null=True, blank=True, max_length=30)
    status_change_time = models.DateField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.offer_status != "SUBMITTED":
            self.status_change_time = date.today()
        if not self.submitted_number:
            new_id = 1
            req = RequiredProject.objects.filter(year=self.year, is_deleted=False)
            if req:
                new_id = req.order_by('-submitted_number')[0]
            self.required_number = new_id
        super(SubmittedProject, self).save()

    def __str__(self):
        return self.reference
