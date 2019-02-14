from django.shortcuts import render
from .models import FoodStall

# Create your views here.

def home(request):
	foodstalls = {
		'foodstalls': FoodStall.objects.all()
	}
	return render(request, 'FoodSwarm/home.html', foodstalls)

def comments(request):
	comments = {
		'comments': Comment.objects.all()
	}
	return render(request, 'FoodSwarm/home.html', comments)


def about(request):
	return render(request, 'FoodSwarm/about.html', {'title': 'About'})