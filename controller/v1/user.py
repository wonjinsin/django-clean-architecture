from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import action, permission_classes

from util.logger import logger
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from rest_framework.serializers import HyperlinkedModelSerializer
from util.permission import ReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


class User(ModelViewSet):
    def list(self, request):
        return HttpResponse("return list")

    def create(self, request):
        return HttpResponse("return create")

    def retrieve(self, request, pk=None):
        return HttpResponse("return retrieve")

    def update(self, request, pk=None):
        return HttpResponse("return retriev")

    def partial_update(self, request, pk=None):
        return HttpResponse("return partial_update")

    def destroy(self, request, pk=None):
        return HttpResponse("return destroy")
