from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
class SignUpForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model = User
		fields = [
			'username',
			'email',
			'first_name',
			'last_name',
		]


class UserEditProfile(forms.ModelForm):
	class Meta:
		model = User
		fields = [
			'email',
			'first_name',
			'last_name',
		]


def register(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('home')
		else:
			return redirect('home')

	else:
		form = SignUpForm()
		return render(request, 'pages/register.html', {'form': form})


def login_in(request):
	if request.method == 'POST':
		form = AuthenticationForm(request,request.POST)
		if form.is_valid():
			login(request, form.get_user())
			return redirect('home')
		else:
			return redirect('home')
	else:
		if request.user.is_authenticated:
			return redirect('home')
		else:

			form = AuthenticationForm()
			return render(request, 'pages/login.html', {'form': form})


@login_required(login_url='/sign-in/')
def log_out(request):
	logout(request)
	return redirect('home')


@login_required(login_url='/sign-in/')
def edit_profile(request):
	if request.method == 'POST':
		form = UserEditProfile(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			return redirect('/')
	else:
		form = UserEditProfile(instance=request.user)
		return render(request, 'pages/edit_profile.html', {'form': form})
