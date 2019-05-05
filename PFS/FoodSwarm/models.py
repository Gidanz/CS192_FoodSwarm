from django.db import models
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class FoodStall(models.Model):
	name = models.CharField(max_length=30, verbose_name='Name of Food Stall')
	description = models.TextField(default = 'N/A', verbose_name='Description')
	location = models.CharField(max_length=100, default = 'N/A', verbose_name='Location (Address)')
	capacity = models.CharField(max_length=15, default = 'N/A', verbose_name='Total Capacity')
	tables = models.CharField(max_length=5, default = 'N/A', verbose_name='Number of Tables')
	chairs = models.CharField(max_length=5, default = 'N/A', verbose_name='Number of Seats')
	operatinghrs = models.CharField(max_length=30, default = 'N/A', verbose_name='Operating Hours')
	peakhrs = models.CharField(max_length=30, default = 'N/A', verbose_name='Peak Hours')
	time_updated = models.DateTimeField(default = timezone.now, verbose_name='Time Created')
	request = models.CharField(max_length=5, default = 'YES', verbose_name='Is this a Food Stall Request?')

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('FoodStall-Detail', kwargs={'pk': self.pk})

class Comment(models.Model):
	CHOICES = (
		('There are some seats available.', 'There are some seats available.'),
		('The Food Stall is full and there are no more seats available.', 'The Food Stall is full and there are no more seats available.'),
		('I don\'t know the current status of the Food Stall.', 'I don\'t know the current status of the Food Stall.')
    )
	fs_name = models.CharField(max_length=30, default = 'N/A', verbose_name='Name of Food Stall')
	date_posted = models.DateTimeField(default = timezone.now, verbose_name='Time Updated')
	status = models.CharField(max_length=100, choices = CHOICES, default = 'I don\'t know the current status of the Food Stall.', verbose_name='Current Food Stall Status')

	def __str__(self):
		return self.fs_name

	def get_absolute_url(self):
		return reverse('Comment-Detail', kwargs={'pk': self.pk})

