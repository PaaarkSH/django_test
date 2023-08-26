from django.db import models
from django.contrib.auth import get_user_model


class Car(models.Model):
    car_id = models.AutoField(primary_key=True)  # image 테이블과 엮기 위한 id 값 명시적으로 선언
    manufacture_year = models.CharField(max_length=8)  # 연식   # 어차피 4자리만 필요할것같아서
    registration_date = models.DateField()  # 최초등록일 (날짜)
    brand = models.CharField(max_length=50)  # 브랜드
    car_type = models.CharField(max_length=50)  # 차종
    car_model = models.CharField(max_length=50)  # 모델
    car_color = models.CharField(
        max_length=20
    )  # 색상  # 색상도 지정된 색상이 있으면 choice 로 구현하는게 좋을것같긴한데 아쉽습니다
    # display 부분은 쓸일은 없지만 그냥 넣어놓겠습니다
    FUEL_CHOICE = (
        ("lpg", "lpg"),
        ("gasoline", "휘발유"),
        ("diesel", "디젤"),
        ("hybrid", "하이브리드"),
        ("electric", "전기"),
        ("bifuel", "바이퓨얼"),
    )
    fuel = models.CharField(max_length=10, choices=FUEL_CHOICE)  # 연료
    TRANSMISSON_CHOICE = (
        ("auto", "자동"),
        ("manual", "수동"),
    )
    transmission = models.CharField(max_length=10, choices=TRANSMISSON_CHOICE)  # 변속기
    mileage = models.PositiveIntegerField()  # 주행거리
    region = models.CharField(max_length=50)  # 지역
    CAR_STATUS_CHOICES = (
        ("pending", "승인대기"),
        ("auction", "경매진행"),
        ("auction_closed", "경매종료"),
        ("completed", "거래완료"),
    )
    car_status = models.CharField(max_length=15, choices=CAR_STATUS_CHOICES)  # 차량 상태
    user_id = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        to_field="user_id",
        db_column="user_id",
    )
    created_date = models.DateTimeField(auto_now_add=True)  # 생성 날짜
    # 모델안에 생산 날짜를 넣는건 별로 좋은 방식은 아닌것같아서 추가
    production_start = models.CharField(max_length=4)  # 생산 시작 날짜
    production_end = models.CharField(max_length=4, blank=True, null=True)  # 생산 종료 날짜
    auction_date = models.DateTimeField(blank=True, null=True)  # 경매 진행 날짜

    class Meta:
        db_table = "car"


class CarImage(models.Model):
    car_id = models.ForeignKey(
        Car, on_delete=models.CASCADE, to_field="car_id", db_column="car_id"
    )
    image = models.CharField(
        max_length=255
    )  # 이미지 주소  # template 을 사용할것도 아닌데 pillow 를 통한 image field 는 사용 안하겠습니다
    created_date = models.DateTimeField(auto_now_add=True)  # 생성 날짜
    update_date = models.DateTimeField(auto_now=True)  # 업데이트 날짜
    seq = models.PositiveIntegerField(
        default=0
    )  # 이미지 순서  # 대표이미지 같은걸 설정해야될수도 있을것같아서 추가했습니다

    class Meta:
        db_table = "image"
