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


class OutcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outcome
        fields = ['id', 'datetime', 'integer']

    def produce(self, data):
        return Outcome.objects.create(**data)
