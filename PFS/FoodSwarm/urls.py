from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='FoodSwarm-Home'),
    path('about/', views.about, name='FoodSwarm-About'),
    path('page/<int:pk>', views.PageDetailView.as_view(), name='FoodSwarm-Page'),
    path('update/<int:pk>', views.UpdateDetailView.as_view(), name='FoodSwarm-Update'),
    path('profile/', views.profile, name='FoodSwarm-Profile'),
    path('favorites/', views.favorites, name='FoodSwarm-Favorites'),
    path('nearme/', views.nearme, name='FoodSwarm-Nearme'),
    path('report/', views.report, name='FoodSwarm-Report'),
    path('request/', views.request, name='FoodSwarm-Request'),
]
