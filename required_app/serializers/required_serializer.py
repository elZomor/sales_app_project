from rest_framework import serializers

from required_app.models import RequiredProject


class RequiredSerializer(serializers.ModelSerializer):
    segment = serializers.CharField()
    required_id = serializers.CharField()

    class Meta:
        model = RequiredProject
        fields = "__all__"
        depth = 1
