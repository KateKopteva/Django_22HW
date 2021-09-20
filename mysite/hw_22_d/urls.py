from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .views import APIEmployeesViewSet


router = DefaultRouter()
router.register('emplo', APIEmployeesViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    ]