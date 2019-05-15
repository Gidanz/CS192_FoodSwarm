from django.urls import path, include
from .views import (
	FoodStallListView, 
	FoodStallDetailView, 
	FoodStallCreateView,
    CommentListView,
	CommentDetailView,
	CommentCreateView
)
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', FoodStallListView.as_view(), name='FoodSwarm-Home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('foodstall/<int:pk>/', FoodStallDetailView.as_view(), name='FoodStall-Detail'),
    path('foodstall/new/', FoodStallCreateView.as_view(), name='FoodStall-Create'),
    path('update/', CommentListView.as_view(), name='FoodSwarm-Update'),
    path('comment/<int:pk>/', CommentDetailView.as_view(), name='Comment-Detail'),
    path('comment/new/', CommentCreateView.as_view(), name='Comment-Create'),
    path('map/', views.home, name='FoodSwarm-Map'),
]
