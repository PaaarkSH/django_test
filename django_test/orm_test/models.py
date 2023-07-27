from django.db import models


class Dept(models.Model):
    dept_code = models.AutoField(primary_key=True)  # pk
    dept_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'dept'


class Emp(models.Model):
    emp_code = models.AutoField(primary_key=True)  # pk
    emp_name = models.CharField(max_length=255)
    dept_code = models.ForeignKey(Dept, on_delete=models.CASCADE)

    class Meta:
        db_table = 'emp'
