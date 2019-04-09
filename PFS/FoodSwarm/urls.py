from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name='FoodSwarm-Home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('about/', views.about, name='FoodSwarm-About'),
    path('page/<int:pk>', views.PageDetailView.as_view(), name='FoodSwarm-Page'),
    path('update/<int:pk>', views.UpdateDetailView.as_view(), name='FoodSwarm-Update'),
    path('profile/', views.profile, name='FoodSwarm-Profile'),
    path('favorites/', views.favorites, name='FoodSwarm-Favorites'),
    path('nearme/', views.nearme, name='FoodSwarm-Nearme'),
    path('report/', views.report, name='FoodSwarm-Report'),
    path('request/', views.request, name='FoodSwarm-Request'),
    path('accounts/', include('django.contrib.auth.urls')),
]
