from django.shortcuts import render
from rest_framework.generics import ListAPIView
from resto.models import Resto, Dishes, District,Sector
from resto.serializers import RestoSerializer, DishesSerializer, DistrictSerializer,SectorSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class RestoListAPIView(ListAPIView):
    queryset = Resto.objects.all()
    serializer_class = RestoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class DishesListAPIView(ListAPIView):
    queryset = Dishes.objects.all()
    serializer_class = DishesSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class DistrictListAPIView(ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class SectorListAPIView(ListAPIView):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]