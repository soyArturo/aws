from employee.models import Employee
from employee.serializers import EmployeeSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import JsonResponse
from utils import get_db_handle


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows employees to be viewed or edited.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
