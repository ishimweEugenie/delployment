from rest_framework import serializers
from Restaurant.models import Resto, Dishes, District, Sector


class RestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resto
        fields = ("name", "owner", "rating", "dishe", "district", "sector")


class DishesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dishes
        fields = ("Dish_name", "price", "co_time", "ingredients", "pictures")


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ("Di_name", "provinse")


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = ("sec_name", "disstrict", "province")
