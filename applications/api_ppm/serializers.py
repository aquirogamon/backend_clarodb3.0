from django.contrib.auth.models import User, Group
from rest_framework import serializers
from applications.api_ppm.models import coreInterface, internetInterface, PeerType, ServiceType, Service


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


class PeerTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PeerType
        fields = ['id', 'url', 'name']


class ServiceTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServiceType
        fields = ['id', 'url', 'name']


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'url', 'name']


class internetInterfaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = internetInterface
        fields = ['id', 'url', 'device', 'port', 'peerType', 'gbpsrx', 'gbpstx', 'gbpsmax',
                  'utilization', 'increase', 'solutionTime', 'comment', 'nameServices', 'deviceIndex', 'created_at']


class coreInterfaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = coreInterface
        fields = ['id', 'url', 'device', 'port', 'serviceType', 'gbpsrx', 'gbpstx', 'gbpsmax',
                  'utilization', 'increase', 'solutionTime', 'comment', 'nameServices', 'deviceIndex', 'created_at']
