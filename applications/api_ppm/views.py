from applications.api_ppm.models import coreInterface, internetInterface, PeerType, ServiceType, Service, internetIP
from applications.api_ppm.serializers import UserSerializer, GroupSerializer, internetInterfaceSerializer, coreInterfaceSerializer, PeerTypeSerializer, ServiceTypeSerializer, ServiceSerializer
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics, permissions
from rest_framework.decorators import action
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PeerTypeViewSet(viewsets.ModelViewSet):
    queryset = PeerType.objects.all()
    serializer_class = PeerTypeSerializer


class ServiceTypeViewSet(viewsets.ModelViewSet):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class internetInterfaceViewSet(viewsets.ModelViewSet):
    queryset = internetInterface.objects.all()
    serializer_class = internetInterfaceSerializer

    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('utilization').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)


class coreInterfaceViewSet(viewsets.ModelViewSet):
    queryset = coreInterface.objects.all()
    serializer_class = coreInterfaceSerializer
