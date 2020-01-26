import requests
import numpy as np

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.views.generic import TemplateView
from rest_framework import viewsets, generics, permissions
from applications.api_ppm.models import coreInterface, internetInterface, PeerType, ServiceType, Service, internetIP
from applications.api_ppm.serializers import UserSerializer, GroupSerializer, internetInterfaceSerializer, coreInterfaceSerializer, PeerTypeSerializer, ServiceTypeSerializer, ServiceSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupView(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PeerTypeView(viewsets.ModelViewSet):
    queryset = PeerType.objects.all()
    serializer_class = PeerTypeSerializer


class ServiceTypeView(viewsets.ModelViewSet):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer


class ServiceView(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class internetInterfaceView(viewsets.ModelViewSet):
    queryset = internetInterface.objects.all()
    serializer_class = internetInterfaceSerializer


class coreInterfaceView(viewsets.ModelViewSet):
    queryset = coreInterface.objects.all()
    serializer_class = coreInterfaceSerializer
