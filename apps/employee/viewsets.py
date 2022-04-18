from apps.employee.serializers import EmployeeSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import JsonResponse
from utils import get_db_handle


class EmployeeViewSet(viewsets.ViewSet):
    def list(self, request):
        db_handle = get_db_handle()
        if db_handle is not None:
            employees = db_handle.employee
            employees_list = employees.find()
            employee_serializer = EmployeeSerializer(employees_list, many=True)
            return Response(employee_serializer.data)
    
    def create(self, request):
        db_handle = get_db_handle()
        if db_handle is not None:
            employees = db_handle.employee
            employee = {
                'name': request.data['name'],
                'age': request.data['age'],
                'salary': request.data['salary']
            }
            employees.insert_one(employee).inserted_id
            employee_serializer = EmployeeSerializer(employee)
            return Response(employee)
        else:
            return Response("Could not connect to database")
