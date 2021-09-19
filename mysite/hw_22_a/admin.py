from django.contrib import admin
from .models import *


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ['name', 'lastname', 'year', 'post']
