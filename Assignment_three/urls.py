"""Assignment_three URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Restaurant import views

urlpatterns = [
    path(r'', views.RestoListAPIView.as_view(), name="Restaurants"),
    path(r'admin/', admin.site.urls),
    path(r'Resto/', views.RestoListAPIView.as_view(), name="Restaurants"),
    path(r'Dishes/', views.DishesListAPIView.as_view(), name="dishes"),
    path(r'District/', views.DishesListAPIView.as_view(), name="districts"),
    path(r'Sector/', views.DishesListAPIView.as_view(), name="sectors")

]
