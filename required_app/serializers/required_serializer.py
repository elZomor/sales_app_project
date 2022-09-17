from rest_framework import serializers

from required_app.models import RequiredProject


class RequiredSerializer(serializers.ModelSerializer):
    segment = serializers.CharField()
    required_id = serializers.CharField()

    class Meta:
        model = RequiredProject
        fields = "__all__"
        depth = 1


class DuplicateProjectSerializer(serializers.Serializer):
    client = serializers.IntegerField()
    required_id = serializers.IntegerField()
    sales_engineer = serializers.ListField(child=serializers.IntegerField(), required=False)
    study_engineer = serializers.ListSerializer(child=serializers.IntegerField(), required=False)
