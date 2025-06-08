from rest_framework import viewsets
from .models import JobApplication
from .serializers import JobApplicationSerializer
from rest_framework.permissions import IsAuthenticated


class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    permission_classes = [IsAuthenticated]  # Secures the API

