from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes

from util.logger import logger
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from rest_framework.serializers import HyperlinkedModelSerializer
from util.permission import ReadOnly
from rest_framework.viewsets import ViewSet


class UserList(ViewSet):
    @permission_classes([ReadOnly])
    def list(self, request, format=None):
        return HttpResponse("return this string")
