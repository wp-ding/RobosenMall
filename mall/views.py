from django.shortcuts import render

# Create your views here.
from libs.models.general import COMPANY
from rest_framework import viewsets
from rest_framework import permissions
from mall.serializers import COMPANYSerializer

class COMPANYViewSet(viewsets.ModelViewSet):
    queryset = COMPANY.objects.all()
    serializer_class = COMPANYSerializer
