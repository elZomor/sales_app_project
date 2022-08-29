from rest_framework.viewsets import ModelViewSet

from required_app.models import RequiredProject
from required_app.serializers import RequiredSerializer


class RequiredViewSets(ModelViewSet):
    serializer_class = RequiredSerializer
    queryset = RequiredProject.objects.all()
