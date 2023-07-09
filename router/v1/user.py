from django.urls import path, include
from rest_framework import routers
from controller.v1.user import User

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'', User, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
