from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class FoodStall(models.Model):
	name = models.CharField(max_length=30)
	description = models.TextField(default = 'N/A')
	location = models.CharField(max_length=100, default = 'N/A')
	capacity = models.CharField(max_length=15, default = 'N/A')
	tables = models.CharField(max_length=5, default = 'N/A')
	chairs = models.CharField(max_length=5, default = 'N/A')
	operatinghrs = models.CharField(max_length=30, default = 'N/A')
	peakhrs = models.CharField(max_length=30, default = 'N/A')
	time_updated = models.DateTimeField(default = timezone.now)

	def __str__(self):
		return self.name

class Comment(models.Model):
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	date_posted = models.DateTimeField(default = timezone.now)
	status = models.CharField(max_length=100, default = 'I don\'t know the current status of the Food Stall.')
		
	def __str__(self):
		return self.status