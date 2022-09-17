from rest_framework import serializers

from required_app.models import SubmittedProject


class SubmittedSerializer(serializers.ModelSerializer):
    required_id = serializers.CharField(source="required_project.required_id")

    class Meta:
        model = SubmittedProject
        fields = "__all__"
