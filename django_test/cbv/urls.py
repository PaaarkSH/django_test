from rest_framework import viewsets
from rest_framework.response import Response

from .models import TestData
from .serailizers import TestDataSerializer


class TestViewSet(viewsets.ViewSet):
    # 해당 변수의 이름은 고정값
    queryset = TestData.objects.all()
    serializer_class = TestDataSerializer

    def create(self, request, *args, **kwargs):  # post
        serializer = TestDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=201)

