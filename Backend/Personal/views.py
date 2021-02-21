from django.shortcuts import render
from operator import attrgetter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.generic import ListView
from django.db.models import Q

from Post.views import get_post_queryset
from Post.models import PostModel

POSTS_PER_PAGE = 2

# Create your views here.

def home(request):
	context = {}
	query = ''
	query = request.GET.get('q', '')
	context['query'] = str(query)

	post_model = sorted(get_post_queryset(query), key=attrgetter('date_updated'), reverse=True)

	page = request.GET.get("page", 1)
	post_model_paginator = Paginator(post_model, POSTS_PER_PAGE)

	try:
		post_model = post_model_paginator.page(page)
	except PageNotAnInteger as e:
		post_model = post_model_paginator.page(POSTS_PER_PAGE)
	except EmptyPage:
		post_model = post_model_paginator.page(post_model_paginator.num_pages)

	context["post_model"] = post_model

	return render(request, "personal/home.html", context)

class home_view(ListView):
	page_kwarg = 'page'
	paginate_by = 2
	context_object_name = 'post_model'
	model = PostModel
	template_name = 'personal/home.html'
	ordering = '-date_published'

	def get_context_data(self, **kwargs):
		search = self.request.GET.get('q', '')
		self.extra_context = {
			'query':str(search)
			}
		print(self.extra_context)
		return super().get_context_data(**kwargs)

	def get_queryset(self):
		search = self.request.GET.get('q', False)
		if search:
			self.querset = self.model.objects.filter(
							Q(caption__icontains=search) |
							 Q(author__username=search)
							 )
			return self.querset
		return super().get_queryset()
