from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .views.required_views import RequiredViewSets

router = DefaultRouter()
router.register(r'engineers', EngineerViewset, basename="engineer")
router.register(r'projects', RequiredViewSets, basename="required")
router.register(r'segments', SegmentViewSets, basename="segments")

urlpatterns = [
    path('', include(router.urls))
]
