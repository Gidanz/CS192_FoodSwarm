from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	TemplateView
)
from .models import FoodStall
from .models import Comment

from django.contrib.auth.forms import UserCreationForm
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
	return render(request, 'FoodSwarm/about.html', comments)


class FoodStallListView(LoginRequiredMixin, ListView):
	context_object_name = 'FoodSwarm-Home'
	template_name = 'FoodSwarm/home.html' 
	queryset = FoodStall.objects.all()
	ordering = ['-time_updated']

	def get_context_data(self, **kwargs):
	    context = super(FoodStallListView, self).get_context_data(**kwargs)
	    context['Comments'] = Comment.objects.all().order_by('-date_posted')
	    context['FoodStalls'] = self.queryset
	    return context


class FoodStallDetailView(LoginRequiredMixin, DetailView):
	context_object_name = 'FoodStall-Detail'
	template_name = 'FoodSwarm/foodstall_detail.html'
	queryset = FoodStall.objects.all()

	def get_context_data(self, **kwargs):
	    context = super(FoodStallDetailView, self).get_context_data(**kwargs)
	    context['Comments'] = Comment.objects.all().order_by('-date_posted')[:4]
	    context['FoodStalls'] = self.queryset
	    return context

class FoodStallCreateView(LoginRequiredMixin, CreateView):
	model = FoodStall
	fields = ['name', 'description', 'location', 'capacity', 'tables', 'chairs', 'operatinghrs', 'peakhrs', 'request']

	def form_valid(self, form):
		return super().form_valid(form)

class CommentListView(LoginRequiredMixin, ListView):
	model = Comment
	template_name = 'FoodSwarm/about.html' 
	context_object_name = 'comments'
	ordering = ['-date_posted']

class CommentDetailView(LoginRequiredMixin, DetailView):
	model = Comment

class CommentCreateView(LoginRequiredMixin, CreateView):
	model = Comment
	fields = ['fs_name', 'status']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
