from django.urls import path, include

urlpatterns = [
    path('', include('router.v1.user')),
]
