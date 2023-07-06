from django.urls import path
from controller.v1.user import UserList

urlpatterns = [
    path('', UserList.as_view({'get': 'list'}), name='user-list'),
]
