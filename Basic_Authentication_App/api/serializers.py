from rest_framework import serializers
from Basic_Authentication_App.models import Employee

class EmployeeSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'