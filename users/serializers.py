from rest_framework import serializers
from djoser.serializers import UserSerializer as DjUserSerializer

class UserSerializer(DjUserSerializer):
    class Meta(DjUserSerializer.Meta):
        pass