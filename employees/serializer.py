from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'title', 'city', 'country', 'owner']
        owner = serializers.ReadOnlyField(source='owner.username')


class UserSerializer(serializers.ModelSerializer):
    employees = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Employee.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'employees']
