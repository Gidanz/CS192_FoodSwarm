from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
	username = forms.CharField(max_length=150, required=True, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
	first_name = forms.CharField(max_length=256, required=False, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
	last_name = forms.CharField(max_length=256, required=False, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
	email = forms.EmailField(max_length=30, required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
	password1 = forms.CharField(min_length=8, max_length=30, required=True, help_text='Your password must contain at least 8 characters.', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
	password2 = forms.CharField(max_length=30, required=True, help_text='Enter the same password as before, for verification.', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']
