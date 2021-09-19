from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response

from .serializers import EmployeesSerializer
from .models import Employees
from rest_framework.decorators import api_view


@api_view(['GET','POST'])
def api_employees(request):
    if request.method == 'GET':
        employees = Employees.objects.filter()
        serializer = EmployeesSerializer(employees, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = EmployeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def api_employees_detail(request, pk):
    employees = Employees.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = EmployeesSerializer(employees)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = EmployeesSerializer(employees, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        employees.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


