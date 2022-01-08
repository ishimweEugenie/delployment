from django.contrib import admin
from django.urls import path,include
from resto import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path(r'', views.RestoListAPIView.as_view(), name="Restaurants"),
    path(r'admin/', admin.site.urls),
    path(r'Resto/', views.RestoListAPIView.as_view(), name="Restaurants"),
    path(r'Dishes/', views.DishesListAPIView.as_view(), name="dishes"),
    path(r'District/', views.DishesListAPIView.as_view(), name="districts"),
    path(r'Sector/', views.DishesListAPIView.as_view(), name="sectors"),

    path('api-auth/', include('rest_framework.urls')),
    path('token/', obtain_auth_token, name='api_token_auth'),

]