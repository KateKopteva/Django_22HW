from rest_framework import status, generics
from rest_framework.viewsets import ModelViewSet
from .serializers import EmployeesSerializer
from .models import *


class APIEmployeesViewSet(ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer



