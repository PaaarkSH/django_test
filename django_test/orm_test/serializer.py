from rest_framework import serializers
from .models import Dept, Emp


class DeptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dept
        fields = ['dept_code', 'dept_name']


class EmpSerializer(serializers.ModelSerializer):
    dept_code = DeptSerializer()  # Nested serializer for ForeignKey field

    class Meta:
        model = Emp
        fields = ['emp_code', 'emp_name', 'dept_code']
