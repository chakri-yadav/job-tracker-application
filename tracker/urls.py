from rest_framework.routers import DefaultRouter
from .views import JobApplicationViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'jobs', JobApplicationViewSet, basename='jobapplication')

urlpatterns = [
    path('', include(router.urls)),
]
