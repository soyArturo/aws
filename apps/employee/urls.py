from django.urls import path, include

from apps.employee.viewsets import EmployeeViewSet
from .views import index, get_employees
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employees')
urlpatterns = [
    path('', include(router.urls)),
]
