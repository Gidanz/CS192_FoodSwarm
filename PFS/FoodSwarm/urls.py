from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='FoodSwarm-Home'),
    path('about/', views.about, name='FoodSwarm-About'),
]
