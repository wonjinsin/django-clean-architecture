from service.user import UserService
from django.http import HttpResponse, JsonResponse
from rest_framework.viewsets import ModelViewSet
from util.logger import logger
from util.permission import ReadOnly


class User(ModelViewSet):
    user_service = UserService()

    def list(self, request):
        logger.info('[Request]')
        self.permission_classes = [ReadOnly]
        self.user_service.get_list()
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
