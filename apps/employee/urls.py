from django.urls import path, include

from employee.viewsets import EmployeeViewSet
from .views import index, get_employees
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
