from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register(r'Resto', RestoListAPIView, basename="Restaurants")
router.register(r'Dish', DishesListAPIView, basename="dishes")
router.register(r'District', DistrictListAPIView, basename="districts")
router.register(r'Sector', SectorListAPIView, basename="sectors")

urlpatterns = format_suffix_patterns([
    # path(r'', RestoListAPIView.as_view({
    #     'get': 'retrieve',
    #     'put': 'update',
    #     'patch': 'partial_update',
    #     'delete': 'destroy',
    #     'post': 'create'
    # }), name="Restaurants"),
    path(r'Resto/', RestoListAPIView.as_view({
        'get': 'list',
        'post': 'create',
    }), name="Restaurants"),
    path(r'Resto/<int:pk>/', RestoListAPIView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'

    }), name="Restaurants"),
    path(r'Dishes/', DishesListAPIView.as_view({
        'get': 'list',
        'post': 'create',
    }), name="dishes"),
    path(r'Dishes/<int:pk>/', DishesListAPIView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name="dishes"),

    path(r'District/', DistrictListAPIView.as_view({
        'get': 'list',
        'post': 'create',
    }), name="districts"),
    path(r'District/<int:pk>/', DistrictListAPIView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
        'post': 'create'
    }), name="districts"),
    path(r'Sector/', SectorListAPIView.as_view({
        'get': 'list',
        'post': 'create',
    }), name="sectors"),

    path(r'Sector/<int:pk>/', SectorListAPIView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
        'post': 'create'
    }), name="sectors"),

]) + router.urls
