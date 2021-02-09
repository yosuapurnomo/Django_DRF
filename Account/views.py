from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm

from Post.models import PostModel
# Create your views here.

def registration_view(request):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email').lower()
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			return redirect('home')
		else:
			context['registration_form'] = form

	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'account/register.html', context)

def logout_view(request):
	logout(request)
	return redirect('/')

def login_view(request):
	context = {}
	user = request.user
	if user.is_authenticated:
		return redirect('home')

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(emaiil=email, password=password)

			if user:
				login(request, user)
				return redirect('home')
	else:
		form = AccountAuthenticationForm()
	context['login_form'] = form

	return render(request, "account/login.html", context)

def account_view(request):
	if not request.user.is_authenticated:
		return redirect('login')

	context = {}
	if request.POST:
		form = AccountUpdateForm(request.POST, instance=request.user)
		if form.is_valid():
			form.initial= {
				"email": request.POST['email'],
				"username": request.POST['username'],
			}
			form.save()
			context['success_message'] = "Updated"

	else:
		form = AccountUpdateForm(
				initial={
						"email": request.user.email,
						"username": request.user.username,
				}	
				)

	context['account_form'] = form

	posts_model = PostModel.objects.filter(author=request.user)
	context['post_model'] = posts_model

	return render(request, "account/account.html", context)

def must_authenticate_view(request):
	return render(request, 'account/must_authenticate.html', {})
