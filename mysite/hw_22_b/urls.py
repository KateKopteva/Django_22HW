from django.urls import path
from .views import *
from .views import APIEmployees, APIEmployeesDetail

urlpatterns = [
    path('employees/', APIEmployees.as_view()),
    path('employees/<int:pk>', APIEmployeesDetail.as_view()),
    ]