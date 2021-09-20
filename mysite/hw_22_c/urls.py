from django.urls import path
from .views import *
from .views import APIEmployees, APIEmployeesDetail

urlpatterns = [
    path('employees_height/', APIEmployees.as_view()),
    path('employees_height/<int:pk>', APIEmployeesDetail.as_view()),
    ]