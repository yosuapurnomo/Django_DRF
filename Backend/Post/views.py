from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.db.models import Q
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

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
	if request.POST:	
		if form.is_valid():
			obj = form.save(commit=False)
			author = Account.objects.filter(email=user.email).first()
			obj.author = author
			obj.save()
			form = CreatePostForm
		return redirect('home')

	context['form'] = form

	return render(request, "post/create.html", context)

class create_view(LoginRequiredMixin, CreateView):
	model = PostModel
	form_class = CreatePostForm
	template_name = 'post/create.html'
	login_url = reverse_lazy('must_authenticate')

	def get_success_url(self):
		return reverse('home')

	def get_initial(self):
		initial = super().get_initial()
		# initial= initial.copy()
		initial['author'] = self.request.user.pk
		return initial

class detail_view(DetailView):
	model = PostModel
	template_name = 'post/detail.html'
	context_object_name = 'post_model'

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

	print("Caption : ", post_model.caption)
	form = UpdatePostForm(
			initial= {
			"caption": post_model.caption,
			"image": post_model.image
			}
		)
	context['form'] = form
	print("context : ", context)
	return render(request, "post/edit.html", context)

class update_view(UpdateView):
	model = PostModel
	form_class = UpdatePostForm
	template_name = 'post/edit.html'
	context_object_name = 'post_model'

	def get_success_url(self, *args, **kwargs):
		return reverse('post:detail', kwargs={'slug':self.request.POST['slug']})

	# def post(self, request, *args, **kwargs):
	# 	self.success_url = reverse('post:detail', kwargs={'slug':request.POST['slug']})
	# 	return super().post(request, *args, **kwargs)

def get_post_queryset(query=None):
	queryset = []
	queries = query.split(" ")
	for q in queries:
		posts = PostModel.objects.filter(caption__icontains=q).distinct()

		for post in posts:
			queryset.append(post)

	return list(set(queryset))




