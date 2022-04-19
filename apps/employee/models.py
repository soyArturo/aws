from django.db import models


class Employee(models.Model):
    """
    Employee model
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    hire_date = models.DateField()
    job_title = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    department = models.CharField(max_length=50)
    supervisor = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
