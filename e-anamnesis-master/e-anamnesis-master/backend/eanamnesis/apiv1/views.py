from django.contrib.auth.models import User
from apiv1.models import Patient
from rest_framework import viewsets
from rest_framework import permissions
from apiv1.serializers import PatientSerializer
from rest_framework.response import Response


class PatientViewSet(viewsets.ViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = []

    def list(self, request):
        queryset = Patient.objects.all()
        serializer = PatientSerializer(queryset, many=True)
        return Response(serializer.data)