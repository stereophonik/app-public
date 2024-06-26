from django.contrib.auth.models import Group, User
from rest_framework import serializers
from project.app.models import Outcome


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class OutcomeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    datetime = serializers.DateTimeField(read_only=True)
    integer = serializers.IntegerField()

    def produce(self, data):
        return Outcome.objects.create(**data)
