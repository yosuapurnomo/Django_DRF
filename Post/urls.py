from django.urls import path, re_path
from .views import (create_post_view, detail_post_view, edit_post_view)

app_name= "post"

urlpatterns = [
	path('create/', create_post_view, name='create'),
	path('<slug>/', detail_post_view, name='detail'),
	path('<slug>/edit', edit_post_view, name='edit'),
]