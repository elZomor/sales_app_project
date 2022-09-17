from rest_framework import serializers

from required_app.models import Segment


class SubSegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segment
        fields = ('id', 'name',)


class SegmentSerializer(serializers.ModelSerializer):
    children = SubSegmentSerializer(many=True, read_only=True)

    class Meta:
        model = Segment
        exclude = ('id', 'name',)
