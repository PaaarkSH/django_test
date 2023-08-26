from rest_framework import serializers
from .models import Car, CarImage


class CarSerializer(serializers.ModelSerializer):
    # user_id 는 user 테이블의 전체 정보까지는 필요없을것같아서 해당 컬럼만
    user_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Car
        fields = [
            "car_id",
            "manufacture_year",
            "registration_date",
            "brand",
            "car_type",
            "car_model",
            "car_color",
            "fuel",
            "transmission",
            "mileage",
            "region",
            "car_status",
            "user_id",
            "created_date",
            "production_start",
            "production_end",
            "auction_date",
        ]


class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = ["car_id", "image", "created_date", "update_date", "seq"]
