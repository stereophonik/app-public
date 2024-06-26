from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from project.app.models import Outcome

from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from project.app.serializers import GroupSerializer, UserSerializer, OutcomeSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

@csrf_exempt
def outcome_list(request):
    if request.method == 'GET':
        outcomes = Outcome.objects.all()
        serializer = OutcomeSerializer(outcomes, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OutcomeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def outcome_detail(request, pk):
    try:
        outcome = Outcome.objects.get(pk=pk)
    except Outcome.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = OutcomeSerializer(outcome)
        return JsonResponse(serializer.data)

    elif request.method == 'DELETE':
        outcome.delete()
        return HttpResponse(status=204)
