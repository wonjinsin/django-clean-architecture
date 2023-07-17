from django.http import HttpResponse
from model.account.serializer import AccountSerializer
from service.user import UserService
from rest_framework.viewsets import ViewSet
from util.logger import logger
from util.response import response
from util.permission import ReadOnly
from rest_framework.request import Request
from rest_framework import status
from django.http import JsonResponse


class User(ViewSet):
    user_service = UserService()

    def list(self, request: Request) -> JsonResponse:
        logger.info('[Request]')
        self.permission_classes = [ReadOnly]
        users = self.user_service.get_list()
        serialized_users = AccountSerializer(users, many=True)
        return response(status.HTTP_200_OK, 'Get Userlist OK', serialized_users)

    def create(self, request: Request):
        return HttpResponse('return create')

    def retrieve(self, request: Request, pk: int):
        return HttpResponse('return retrieve')

    def update(self, request: Request, pk: int):
        return HttpResponse('return retriev')

    def partial_update(self, request: Request, pk: int):
        return HttpResponse('return partial_update')

    def destroy(self, request: Request, pk: int):
        return HttpResponse('return destroy')
