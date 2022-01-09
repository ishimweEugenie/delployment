from django.contrib import admin
from django.urls import path,include
from resto import views

urlpatterns = [
    path(r'', views.RestoListAPIView.as_view(), name="Restaurants"),
    path(r'Resto/', views.RestoListAPIView.as_view(), name="Restaurants"),
    path(r'Dishes/', views.DishesListAPIView.as_view(), name="dishes"),
    path(r'District/', views.DishesListAPIView.as_view(), name="districts"),
    path(r'Sector/', views.DishesListAPIView.as_view(), name="sectors"),


]