from rest_framework.viewsets import ModelViewSet

from required_app.models import Engineer
from required_app.serializers.engineer_serializer import EngineerSerializer


class EngineerViewset(ModelViewSet):
    serializer_class = EngineerSerializer
    queryset = Engineer.objects.all()
