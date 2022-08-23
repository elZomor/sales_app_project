from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'engineers', EngineerViewset, basename="engineer")

urlpatterns = [
    path('', include(router.urls))
]
