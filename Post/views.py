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
	context = {}
	user = request.user
	if not user.is_authenticated:
		return redirect('must_authenticate')

	post_model = get_object_or_404(PostModel, slug=slug)

	if post_model.author != user:
		return HttpResponse("You are not the author of the post")

	if request.POST:
		form = UpdatePostForm(request.POST or None, request.FILES or None, instance=post_model)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			context["success_message"] = "Update"
			post_model = obj

	form = UpdatePostForm(
			initial= {
			"caption": post_model.caption,
			"image": post_model.image
			}
		)

	context['form']: form
	return render(request, "blog/edit.html", context)

def get_post_queryset(query=None):
	queryset = []
	queries = query.split(" ")
	for q in queries:
		posts = PostModel.objects.filter(caption__icontains=q).distinct()

		for post in posts:
			queryset,append(post)

	return list(set(queryset))




