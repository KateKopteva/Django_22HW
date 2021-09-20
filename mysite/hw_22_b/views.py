from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import EmployeesSerializer
from .models import Employees
from rest_framework.decorators import api_view


class APIEmployees(APIView):
    def get(self, request):
        employees = Employees.objects.filter()
        serializer = EmployeesSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class APIEmployeesDetail(APIView):
    def get(self, request, pk):
        employees = Employees.objects.get(pk=pk)
        serializer = EmployeesSerializer(employees)
        return Response(serializer.data)

    def put(self, request, pk):
        employees = Employees.objects.get(pk=pk)
        serializer = EmployeesSerializer(employees, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employees = Employees.objects.get(pk=pk)
        employees.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



