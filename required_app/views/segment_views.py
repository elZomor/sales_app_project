from rest_framework.viewsets import ModelViewSet

from required_app.models import Segment
from required_app.serializers import SegmentSerializer


class SegmentViewSets(ModelViewSet):
    serializer_class = SegmentSerializer
    queryset = Segment.objects.filter(parent__isnull=True)
