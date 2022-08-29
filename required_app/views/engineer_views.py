import json

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from required_app.models import Engineer
from required_app.serializers.engineer_serializer import EngineerSerializer


class EngineerViewset(ModelViewSet):
    serializer_class = EngineerSerializer
    queryset = Engineer.objects.all()

    @action(methods=["get"], detail=False)
    def all(self, request, *args, **kwargs):
        x = "fff"
        print("HEEO", flush=True)
        return Response(data={"data": x}, status=status.HTTP_200_OK)
