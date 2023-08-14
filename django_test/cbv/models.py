from django.db import models


class TestData(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    subscribe = models.CharField(max_length=255)
    number = models.IntegerField()

    class Meta:
        db_table = 'test_data'

