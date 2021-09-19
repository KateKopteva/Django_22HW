from rest_framework import serializers
from .models import *


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('name', 'lastname', 'year', 'post')