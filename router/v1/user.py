from django.urls import path, include
from rest_framework import routers
from controller.v1.user import User

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'user', User, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
