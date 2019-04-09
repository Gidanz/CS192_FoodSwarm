from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from .models import FoodStall

from FoodSwarm.models import FoodStall

# Create your views here.

def home(request):
	title = "Home"
	foodstalls = {
		'foodstalls': FoodStall.objects.all()
	}
	return render(request, 'FoodSwarm/home.html', foodstalls)

class PageDetailView(DetailView):
	template_name = 'FoodSwarm/foodstall_detail.html'
	model = FoodStall

class UpdateDetailView(DetailView):
	template_name = 'FoodSwarm/update_detail.html'
	model = FoodStall

def comments(request):
	comments = {
		'comments': Comment.objects.all()
	}
	return render(request, 'FoodSwarm/home.html', comments)

def about(request):
	return render(request, 'FoodSwarm/about.html', {'title': 'About'})

def profile(request):
	return render(request, 'FoodSwarm/profile.html', {'title': 'Profile'})

def favorites(request):
	raise Http404('page does not exist')

def nearme(request):
    raise Http404('page does not exist')

def report(request):
	raise Http404('page does not exist')

def request(request):
	raise Http404('page does not exist')
