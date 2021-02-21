from django.urls import path
from .views import (api_detail_view, api_update_view, 
					api_delete_view, api_create_view, 
					listPost, createPost, updatePost, 
					detailPost, deletePost)

app_name = 'api_post'
urlpatterns = [
	path('list', listPost.as_view(), name='api_list'),
	path('<slug>/', api_detail_view, name='api_detail'),
	path('<slug>/detail/', detailPost.as_view(), name='api_detail'),
	path('<slug>/update/', api_update_view, name='api_update'),
	path('<slug>/update_api/', updatePost.as_view(), name='api_update'),
	path('<slug>/delete/', api_delete_view, name='api_delete'),
	path('<slug>/delete_api/', deletePost.as_view(), name='api_delete'),
	path('create', api_create_view, name='api_create'),
	path('create_api', createPost.as_view(), name='api_create'),
]