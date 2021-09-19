from django.urls import path
from .views import *

urlpatterns = [
    path('api_view/', api_employees),
    path('api_view/<int:pk>', api_employees_detail),
]