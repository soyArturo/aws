from rest_framework import serializers


class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    age = serializers.CharField(max_length=100)
    salary = serializers.CharField(max_length=100)
