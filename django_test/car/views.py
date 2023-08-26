from django.db.models import Q, F, Count
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination

from .models import Car, CarImage
from .serializers import CarSerializer, CarImageSerializer
from library.lib import get_request_data
from django.utils import timezone


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]  # 유효성 검사
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        """
        get 으로 전체 차량을 조회할때 필터링 걸도록 오버라이드
        """

        queryset = Car.objects.exclude(
            car_status="pending"
        )  # 기본적으로 승인대기를 제외한 데이터만 조회하도록
        params = get_request_data(request)

        car_status = params.get("car_status", "")
        order = params.get("order", "")
        brand = params.get("brand", "")
        car_type = params.get("car_type", "")
        model = params.get("model", "")

        # 경매진행중 거래완료 경매종료 중 하나만 볼 수 있게
        # pdf 에 그냥 다 보여주시긴 하고 필터링 하는 버튼은 없어보이는데 그냥 혹시 몰라서 넣었습니다
        if car_status:
            queryset = queryset.filter(car_status=car_status)

        if order == "oldest":  # 오래된 순
            queryset = queryset.order_by("created_date")
        else:  # 최근순을 디폴트로 하겠습니다
            queryset = queryset.order_by("-created_date")

        # 브랜드나 차종이나 모델로 필터링 하기 위해 추가
        if brand or car_type or model:
            filter_condition = Q()
            if brand:
                filter_condition &= Q(brand=brand)
            if car_type:
                filter_condition &= Q(car_type=car_type)
            if model:
                filter_condition &= Q(car_model=model)
            queryset = queryset.filter(filter_condition)

        page = self.paginate_queryset(queryset)  # 페이징된 결과 가져오기
        if page:
            # 페이지가 들어올경우 페이징 처리
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        # 아닐경우 그냥 조회
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_filtered_counts(self, queryset, group_by_field):
        """
        그루핑 정보를 받아서 카운트를 셀려고 만든 함수
        """
        return queryset.values(group_by_field).annotate(count=Count("car_id"))

    @action(detail=False, methods=["GET"], url_path="filtered_data")
    def filtered_data(self, request):
        """
        차종 검색 필터 API 추가
        """
        params = get_request_data(request)
        filter_column = params.get("filter_column", "all")
        brand_name = params.get("brand_name")
        car_type_name = params.get("car_type_name")
        queryset = Car.objects.all()
        if brand_name:
            # brand name 이 이미 파라미터로 들어올 경우는 brand_name 으로 필터링
            queryset = queryset.filter(brand=brand_name)

        if filter_column == "brand":
            # brand 로만 필터링 할 경우는 car_type 의 count 출력
            data = self.get_filtered_counts(queryset, "car_type")
            return Response(data, status=status.HTTP_200_OK)
        elif filter_column == "car_type" and brand_name:
            # car_type 으로 파라미터가 들어올 경우는 model 명으로 그루핑
            queryset = queryset.filter(car_type=car_type_name)
            data = self.get_filtered_counts(queryset, "model")
            return Response(data, status=status.HTTP_200_OK)
        elif filter_column == "all":
            # 디폴트로 브랜드명을 기준으로 카운트 하는 로직으로 추가
            data = self.get_filtered_counts(queryset, "brand")
            return Response(data, status=status.HTTP_200_OK)

        return Response(data=[], status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        # 생성시 user 정보를 바로 반영하기 위해서 추가
        # 문제될 시 삭제
        serializer.save(user_id=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        params = get_request_data(self.request)
        car_status = params.get("car_status")

        # 만약에 경매 진행으로 업데이트 할때 경매 진행 날짜에 현재 날짜 저장
        if car_status == "auction":
            instance.car_status = car_status
            instance.auction_date = timezone.now()  # db 시간 날짜로 저장
            instance.save()

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)


class CarImageViewSet(viewsets.ModelViewSet):
    queryset = CarImage.objects.all()
    serializer_class = CarImageSerializer
    permission_classes = [permissions.IsAuthenticated]  # 유효성 검사

    # 차량 사진은 5장 이상이라고 말씀해주셔서 5장이 안될경우 예외처리 하겠습니다
    def create(self, request, *args, **kwargs):
        params = get_request_data(request=request)
        images = params.get("images", "")
        image_list = str(images).split(",")
        if not image_list or len(image_list) < 5:
            return Response(
                data={"message": "5개 이상의 이미지가 필요합니다"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        car_id = params.get("car_id", "")
        if not car_id or not str(car_id).isdigit():
            return Response(
                data={"message": "유효하지 않은 차량 정보입니다"}, status=status.HTTP_400_BAD_REQUEST
            )

        # for 반복을 돌아서 insert 하는건 트랜잭션 처리하기 불편함
        data_list = [
            {"car_id": int(car_id), "image": image, "seq": i}
            for i, image in enumerate(image_list)
        ]
        serializer = self.get_serializer(data=data_list, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            data={
                "message": "이미지 생성에 성공하셨습니다",
            },
            status=status.HTTP_201_CREATED,
        )

    def list(self, request, *args, **kwargs):
        """
        image 데이터 대량 출력을 위한 list 함수 구현
        0 번 seq 사진을 대표 사진이라고 보고 오름 차순으로 구현
        """
        car_id = request.query_params.get("car_id")
        if not car_id or not car_id.isdigit():
            return Response(
                data={"message": "유효하지 않은 차량 정보입니다"}, status=status.HTTP_400_BAD_REQUEST
            )

        images = CarImage.objects.filter(car_id=car_id).order_by(
            "seq"
        )  # 오름 차순으로 이미지 출력
        serializer = self.get_serializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
