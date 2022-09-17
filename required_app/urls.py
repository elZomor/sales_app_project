from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .views.required_views import RequiredViewSets
from .views.submitted_views import SubmittedViewSets

router = DefaultRouter(trailing_slash=False)
router.register(r'engineers', EngineerViewset, basename="engineer")
router.register(r'projects', RequiredViewSets, basename="required")
router.register(r'segments', SegmentViewSets, basename="segments")
router.register(r'submitted', SubmittedViewSets, basename="Submitted")

urlpatterns = [
    path('', include(router.urls))
]
