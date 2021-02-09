from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse

from .models import PostModel
from .forms import CreatePostForm, UpdatePostForm
from Account.models import Account

# Create your views here.

def create_post_view(request):
	context = {}

	user = request.user
	if not user.is_authenticated:
		return redirect('must_authenticate')

	form = CreatePostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		author = Account.objects.filter(email=user.email).first()
		obj.author = author
		obj.save()
		form = CreatePostForm

	context['form'] = form

	return render(request, "post/create.html", context)

def detail_post_view(request, slug):
	context = {}

	post_model = get_object_or_404(PostModel, slug=slug)
	context['post_model'] = post_model

	return render(request, 'post/detail.html', context)

def edit_post_view(request, slug):
	pass