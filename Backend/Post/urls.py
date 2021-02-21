from django.urls import path, re_path
from .views import (create_post_view, edit_post_view, create_view, detail_view, update_view)

app_name= "post"

urlpatterns = [
	# path('create/', create_post_view, name='create'),
	path('create/', create_view.as_view(), name='create'),
	# path('<slug>/', detail_post_view, name='detail'),
	path('<slug>/', detail_view.as_view(), name='detail'),
	# path('<slug>/edit', edit_post_view, name='edit'),
	path('<slug:slug>/edit', update_view.as_view(), name='edit'),
]