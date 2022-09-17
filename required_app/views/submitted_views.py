from rest_framework.viewsets import ModelViewSet

from required_app.models import SubmittedProject
from required_app.serializers.submitted_serializer import SubmittedSerializer


class SubmittedViewSets(ModelViewSet):
    serializer_class = SubmittedSerializer
    queryset = SubmittedProject.objects.all()
