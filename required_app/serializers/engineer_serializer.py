from rest_framework import serializers

from required_app.models import Engineer


class EngineerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engineer
        fields = "__all__"