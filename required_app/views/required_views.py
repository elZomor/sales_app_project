from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.utils.timezone import now

from required_app.models import RequiredProject, Client
from required_app.serializers import RequiredSerializer
from required_app.serializers.required_serializer import DuplicateProjectSerializer


class RequiredViewSets(ModelViewSet):
    serializer_class = RequiredSerializer
    queryset = RequiredProject.objects.all()

    @action(detail=False, methods=["POST"])
    def duplicate_project(self, request):
        data = request.data
        print("Jii", flush=True)
        serializer = DuplicateProjectSerializer(data=data)
        if not serializer.is_valid():
            return Response(data={"code": "Invalid Input", "message": "{}".format(serializer.errors)},
                            status=400)
        project = RequiredProject.objects.filter(id=serializer.data['required_id']).last()
        if not project:
            return Response(data={"code": "Not Found",
                                  "message": "No project with required_id: {}".format(serializer.data['required_id'])},
                            status=404)
        client = Client.objects.filter(id=serializer.data['client']).last()
        if not client:
            return Response(data={"code": "Not Found",
                                  "message": "No Client with id: {}".format(serializer.data['client'])},
                            status=404)

        project.make_clone(attrs={
            'required_number': None,
            'client': client,
            'required_date': now(),

        })

        return Response(data={"code": "Successful",
                              "message": "a new project has been added successfully!"},
                        status=201)
