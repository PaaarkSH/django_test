from .models import Dept, Emp
from django import forms


class DeptForm(forms.ModelForm):
    class Meta:
        model = Dept
        fields = ['dept_code', 'dept_name']


class EmpForm(forms.ModelForm):
    class Meta:
        model = Emp
        fields = ['emp_code', 'emp_name', 'dept_code']

